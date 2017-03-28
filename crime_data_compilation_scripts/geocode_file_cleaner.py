from geopy.geocoders import Nominatim
import json
from pprint import pprint
from pygeocoder import Geocoder

clean_crime_data = open("crime_data_geocode.txt", 'w+')
null_data_lines = open("crime_null_data.txt", 'w+')

count=0
with open('crime_geocoded_raw.txt') as infile:
    for line in infile:
        if "None" in line:
            print("NONE")
            null_data_lines.write(bytes(count))
            null_data_lines.write("\n")
            count+=1
        else:
            clean_crime_data.write(line)
            count+=1
