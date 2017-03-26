from geopy.geocoders import Nominatim
import json
from pprint import pprint
from pygeocoder import Geocoder

geolocator = Nominatim()

crime_data_compile = open("crime_geocoded_raw.txt", 'w+')
null_data_lines = open("crime_null_data.txt", 'w+')

line_count = 0
with open('crime_data_clean.txt') as infile:
    for line in infile:
        theline = line.strip().split(',')[2] + " Tuscaloosa, AL 35487"
        print theline
        location = geolocator.geocode(theline)
        if location:
            lat=location.latitude
            lon=location.longitude
        else :
            lat = None
            lon = None
        if(lat==str("None") or lon == str("None")):
            printf("NONE")
            null_data_lines.write(count)
            null_data_lines.write("\n")


        else:
            descript = line.strip().split(',')[0]
            date = line.strip().split(',')[1]
            address = line.strip().split(',')[2]
            crime_data_compile.write(bytes(descript))
            crime_data_compile.write(str(","))
            crime_data_compile.write(bytes(date))
            crime_data_compile.write(str(","))
            crime_data_compile.write(bytes(lat))
            crime_data_compile.write(str(","))
            crime_data_compile.write(bytes(lon))
            crime_data_compile.write(str(","))
            crime_data_compile.write(bytes(address))
            crime_data_compile.write("\n")
