# @Author: Miclain K <user>
# @Date:   03-25-2017
# @Last modified by:   user
# @Last modified time: 03-25-2017


from geopy.geocoders import Nominatim
import json
from pprint import pprint

geolocator = Nominatim()

all_addresses = []
all_lats = []
all_longs = []

all_names = {}
count=0
outfile = open('apartment_summary_vectors.json','w')
with open('apartment_latlong_clean.txt') as infile:
    all_lats = [line.split(',')[0] for line in infile.readlines()]
with open('apartment_latlong_clean.txt') as infile2:
    all_longs = [line.strip().split(',')[1] for line in infile2.readlines()]
with open('apartment_addresses_clean.txt') as f:
    all_addresses = [line.strip() for line in f.readlines()]

with open('apartment_names_clean.txt') as names:
    all_names = [line.strip() for line in names.readlines()]


    #bit_vector = [1 if p in app_permission_map[app_name] else 0 for p in all_permissions]
    #all_apps[app_name] = {'vector': bit_vector, 'malicious': app_malicious_map[app_name]}
    #    all_names[line] = {'address': all_addresses[count],'lat_long': all_lat_longs[count+1s]}
    #    count+=1
    for name in all_names:
        json.dump({'name': name, 'address': all_addresses[count], 'lats': all_lats[count+1],'longs': all_longs[count+1]}, outfile)
        outfile.write(",")

        count=count+1
#for x in all_names:
#    for y in all_names[x]:
#            print(all_names[x][y],x)
    #
#with open('complex_names_cleaned.txt') as names:
#    for line in names:
        #bit_vector = [1 if p in app_permission_map[app_name] else 0 for p in all_permissions]
        #all_apps[app_name] = {'vector': bit_vector, 'malicious': app_malicious_map[app_name]}
#        all_names[line] = {}

#        with open('lat_long_apartments.txt') as infile:
#            with open('apartment_summary_vectors.json') as outfile:
#                json.dump({'name': all_names, 'address': all_addresses, 'lat': all_lats, 'long': all_longs}, outfile)
