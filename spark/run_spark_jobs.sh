#!/bin/bash

echo "loading modules"
module load python/gnu/3.6.5
module load spark/2.4.0

cd ../data/"Harvard Economic Tracker Data"/data

echo "removing old files"
rm covid_employment.csv
hfs -rm "COVID - State - Daily.csv"
hfs -rm "Employment Combined - State.csv"
hfs -rm usa-state-ansi-fips.csv
hfs -rm -r covid_employment.out

echo "uploading new files"
hfs -put ./"COVID - State - Daily.csv"
hfs -put ./"Employment Combined - State - Daily.csv"
hfs -put ../us-state-ansi-fips.csv

cd ../../../../spark

echo "running spark job 1: Join COVID and Employment Data from Harvard Economic Tracker"
spark-submit --conf spark.pyspark.python=/share/apps/python/3.6.5/bin/python ./joined_covid_employment.py /user/{net_id}/"COVID - State - Daily.csv" 
/user/{net_id}/"Employment Combined - State - Daily.csv"

cd ../data/spark_datasets

echo "getting spark job 1 output"
hfs -getmerge covid_employment.out covid_employment.csv
echo "output saved locally in data/spark_datasets/ directory as covid_employment.csv"

echo "running spark job 2: Join covid_employment.csv with FIPS data to get state abbreviations"
hfs -put covid_employment.csv
spark-submit --conf spark.pyspark.python=/share/apps/python/3.6.5/bin/python ./april_covid_fips.py /user/{net_id}/covid_employment.csv
/user/{net_id}/usa-state-ansi-fips

cd ../data/spark_datasets

echo "getting spark job 2 output"
hfs -getmerge covid_employment_fips.out covid_employment_fips.csv
echo "output saved locally in data/spark_datasets/ directory as covid_employment_fips.csv"

echo "Spark Job Complete!"