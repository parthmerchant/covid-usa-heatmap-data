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

# Get covid_employment.csv joined file from previous spark job
joined_data = sc.textFile(sys.argv[1])

# Get FIPS State data
fips_data = sc.textFile(sys.argv[2])

# Encode the data
dates_encoded = joined_data.map(lambda line: line.encode("utf-8"))
fips_encoded = fips_data.map(lambda line: line.encode("utf-8"))

# Get data for only April 1st, 2020
april_data = dates_encoded.filter(lambda line: "2020,4,1," in ','.join(line.split(",")[0:3]))

# Map state as key
april_states_keys = april_data.map(lambda line: (line.split(",")[3], ','.join(line.split(",")[4:7])+','+line.split(",")[17]))
# Map state as key for FIPS
fips_keys = fips_encoded.map(lambda line: (line.split(",")[1], line.split(",")[2]))

# Join to get state abbreviation along with FIPS
states_fips = april_states_keys.join(fips_keys)

# Sort by key
sorted_states_fips = states_fips.sortByKey()

# Combine tuple into .csv format
final_format = sorted_keys.map(lambda line: line[0]+','+line[1][0]+','+line[1][1])

# Save as textFile
final_format.saveAsTextFile("covid_employment_fips.out")