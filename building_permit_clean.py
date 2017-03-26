from geopy.geocoders import Nominatim
import json
from pprint import pprint


all_status = []
all_address = []
all_lats = []
all_longs = []

count=0

outfile = open('building_permit_clean.json','w')


    #print all_status
with open('building_permit_filtered.txt') as infile2:
    all_address = [line.strip('\"').split(',')[15:16] for line in infile2.readlines()]
with open('building_permit_filtered.txt') as infile2:
    all_status= [line.strip('\"').split(',')[14:15] for line in infile2.readlines()]
with open('building_permit_filtered.txt') as lats:
    all_lats = [line.strip('\"').split(',')[55:56] for line in lats.readlines()]
with open('building_permit_filtered.txt') as longs:
    all_longs = [line.strip('\"').split(',')[56:57] for line in longs.readlines()]

outfile.write("[")

for address in all_address:

    json.dump({'address': address, 'status': all_status[count],'lats': all_lats[count],'longs': all_longs[count]}, outfile)
    outfile.write(",")

    count=count+1
outfile.write("]")
