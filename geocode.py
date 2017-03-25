from geopy.geocoders import Nominatim
import json
geolocator = Nominatim()


with open('run_results.json') as infile:
        list_of_apartments = json.load(infile)
        for name in list_of_apartments:
            print name
            location = geolocator.geocode("")
            print((location.latitude, location.longitude))
