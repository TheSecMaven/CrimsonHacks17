from geopy.distance import vincenty
from geopy.geocoders import Nominatim
import json
from pprint import pprint

all_lats = []
all_longs = []
list_of_crimes = []
apartments = []
apartments_out = []
outfile = open('apartment_summary_vectors_with_crimes.json', 'w+')

with open('crime_data_clean.json') as crime_data1:
    crime_data = json.load(crime_data1)
    with open('apartment_summary_vectors.json') as apartment_data1:
        apartment_data = json.load(apartment_data1)
        for apartment in apartment_data:
            apartment.update({"crimes":[]})
            apartments.append(apartment)

        for crime in crime_data:

            crime_lat_long = tuple((crime['lats'], crime['longs']))
            for i, apartment in enumerate(apartment_data):
                apartment_long_lat = (apartment['lats'],apartment['longs'])
                if (vincenty(crime_lat_long, apartment_long_lat).miles) <= .25:
                    apartments[i]["crimes"].append(crime)


json.dump(apartments, outfile)
