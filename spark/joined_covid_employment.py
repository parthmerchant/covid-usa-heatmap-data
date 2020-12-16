import sys
from csv import reader
from pyspark import SparkContext

if len(sys.argv) != 3:
    print("Missing Files")
    exit(-1)

sc = SparkContext()

covid = sc.textFile(sys.argv[1])

employment = sc.textFile(sys.argv[2])

# Map by YYYY,M,DD,statesfips as the key
covid_keys = covid.map(lambda line: (",".join(line.split(",")[:4]),','.join(line.split(",")[4:])))
employment_keys = employment.map(lambda line: (",".join(line.split(",")[:4]),','.join(line.split(",")[4:])))

# Join Covid and Employment by keys
joined_keys = covid_keys.join(employment_keys)

# Sort by Key 
sorted_keys = joined_keys.sortByKey()

# Reformat the output as comma separated
joined_format = sorted_keys.map(lambda line: line[0]+','+line[1][0]+','+line[1][1])

date_reformat = joined_format.map(lambda line: '-'.join(line.split(",")[:3])+','+",".join(line.split(",")[3:]))

# Save as textFile
date_reformat.saveAsTextFile("covid_employment4.out")