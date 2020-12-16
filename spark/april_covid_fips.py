import sys
from csv import reader
from pyspark import SparkContext

# Check number of arguments
# Argument 1: joined_covid_employment.csv
# Argument 2: us-state-ansi-fips.csv
if len(sys.argv) != 3:
    print("Missing Files")
    exit(-1)

# Initialize SparkContext
sc = SparkContext()

joined_data = sc.textFile(sys.argv[1])

fips_data = sc.textFile(sys.argv[2])

dates_encoded = joined_data.map(lambda line: line.encode("utf-8"))

fips_encoded = fips_data.map(lambda line: line.encode("utf-8"))

april_data = dates_encoded.filter(lambda line: "2020,4,1," in ','.join(line.split(",")[0:3]))

april_states_keys = april_data.map(lambda line: (line.split(",")[3], ','.join(line.split(",")[4:7])+','+line.split(",")[17]))

fips_keys = fips_encoded.map(lambda line: (line.split(",")[1], line.split(",")[2]))

states_fips = april_states_keys.join(fips_keys)

sorted_states_fips = states_fips.sortByKey()

final_format = sorted_keys.map(lambda line: line[0]+','+line[1][0]+','+line[1][1])

final_format.saveAsTextFile("covid_employment_fips.out")