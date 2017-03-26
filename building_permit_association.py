from geopy.distance import vincenty
from geopy.geocoders import Nominatim
import json
from pprint import pprint

all_lats = []
all_longs = []
list_of_crimes = []
apartments = []
apartments_out = []
outfile = open('apartment_summary_vectors_with_crimes_and_permits.json', 'w+')

with open('building_permit_cleaned_up.json') as building_permits:
    permit_data = json.load(building_permits)
    with open('apartment_summary_vectors.json') as apartment_data1:
        apartment_data = json.load(apartment_data1)
        for apartment in apartment_data:
            apartment.update({"permits":[]})
            apartments.append(apartment)

        for permit in permit_data:

            permit_lat_long = tuple((permit['lats'], permit['longs']))
            print permit_lat_long

    #        for i, apartment in enumerate(apartment_data):
    #            apartment_long_lat = (apartment['lats'],apartment['longs'])
    #            if (vincenty(permit_lat_long, apartment_long_lat).miles) <= .25:
    #                apartments[i]["permits"].append(permit)

for a in apartments:
    json.dump({'name': a["name"], 'address': a["address"], 'lats': a["lats"], 'longs': a["longs"], 'crimes': a["crimes"]}, outfile)
    outfile.write(",")
