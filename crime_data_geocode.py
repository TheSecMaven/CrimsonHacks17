from geopy.geocoders import Nominatim
import json
from pprint import pprint

geolocator = Nominatim()

crime_data_compile = open("crime_data_clean.txt", 'w+')

with open('crime_data_clean.txt') as infile:
    for line in infile:
        location = geolocator.geocode(line)
        if location:
            lat=location.latitude
            lon=location.longitude
        else :
            lat = None
            long = None
        if(lat=="None" || long = "None"){
        print("Line to be deleted ")
        }
        list_of_apartments.write(bytes(lat))
        list_of_apartments.write(str(","))
        list_of_apartments.write(bytes(lon))
        list_of_apartments.write("\n")
