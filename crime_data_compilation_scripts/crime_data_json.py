from geopy.geocoders import Nominatim
import json
from pprint import pprint


all_types = []
all_dates = []
all_lats = []
all_longs = []
all_address = []
count=0

outfile = open('crime_data_clean.json','w')


    #print all_status
with open('crime_data_geocode.txt') as infile2:
    all_types = [line.strip('\"').split(',')[0] for line in infile2.readlines()]
with open('crime_data_geocode.txt') as infile2:
    all_dates= [line.strip('\"').split(',')[1] for line in infile2.readlines()]
with open('crime_data_geocode.txt') as lats:
    all_lats = [line.strip('\"').split(',')[2] for line in lats.readlines()]
with open('crime_data_geocode.txt') as longs:
    all_longs = [line.strip('\"').split(',')[3] for line in longs.readlines()]
with open('crime_data_geocode.txt') as longs:
    all_address = [line.strip().split(',')[4] for line in longs.readlines()]

outfile.write("[")

for address in all_address:

    json.dump({'address': address,'type': all_types[count], 'date': all_dates[count],'lats': all_lats[count],'longs': all_longs[count]}, outfile)
    outfile.write(",")

    count=count+1
outfile.write("]")
