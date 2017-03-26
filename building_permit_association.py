from geopy.distance import vincenty
from geopy.geocoders import Nominatim
import json
from pprint import pprint
from string import digits

all_lats = []
all_longs = []
apartments = []
apartments_out = []
outfile = open('apartment_summary_vectors_with_crimes_and_permits.json', 'w+')

with open('building_permit_cleaned_up.json') as building_permits:
    permit_data = json.load(building_permits)
    with open('apartment_summary_vectors_with_crimes.json') as apartment_data1:
        apartment_data = json.load(apartment_data1)
        for apartment in apartment_data:
            apartment.update({"permits":[]})
            apartments.append(apartment)

        for permit in permit_data:
            latit =  (permit['lats'])
            print latit[0]

          #  latter = latit[0:len(latit)]
            #print latter
            longit =  (permit['longs'])
           # longer = longit[0:len(longit)]
            #print longer

            permit_lat_long = tuple((latit[0], longit[0]))

            for i, apartment in enumerate(apartment_data):
                apartment_long_lat = (apartment['lats'],apartment['longs'])
                if (vincenty(permit_lat_long, apartment_long_lat).miles) <= .20:
                    apartments[i]["permits"].append(permit)

for a in apartments:
    json.dump({'name': a["name"], 'address': a["address"], 'lats': a["lats"], 'longs': a["longs"], 'crimes': a["crimes"],'permits': a["permits"]}, outfile)
    outfile.write(",")
