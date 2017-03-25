from geopy.geocoders import Nominatim
import json
from pprint import pprint

geolocator = Nominatim()


with open('run_results.json') as infile:
    list_of_apartments = json.load(infile)
    for line in list_of_apartments:
        print (line)
        #pprint (list_of_apartments)
#    location = geolocator.geocode("")
        #print((location.latitude, location.longitude))
