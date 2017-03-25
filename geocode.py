from geopy.geocoders import Nominatim
import json
from pprint import pprint

geolocator = Nominatim()


with open('run_results.txt') as infile:
    for line in infile:
        location = geolocator.geocode(line)
        with open('lat_long_apartments.json','w') as list_of_apartments:

            list_of_apartments.write(location)
