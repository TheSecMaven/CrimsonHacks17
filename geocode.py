from geopy.geocoders import Nominatim
import json
from pprint import pprint

geolocator = Nominatim()

list_of_apartments = open("lat_long_apartments.txt", 'w+')

with open('run_results.txt') as infile:
    for line in infile:
        location = geolocator.geocode(line)
        if location:
            lat=location.latitude
            lon=location.longitude
        else :
            lat = None
            long = None
        list_of_apartments.write(bytes(lat))
        list_of_apartments.write(str(","))
        list_of_apartments.write(bytes(lon))
        list_of_apartments.write("\n")
