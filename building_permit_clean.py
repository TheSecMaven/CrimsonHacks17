from geopy.geocoders import Nominatim
import json
from pprint import pprint

geolocator = Nominatim()

all_status = []
all_address = []
all_lats = []
all_longs = []

count=0

outfile = open('building_permit_clean.txt','w')
with open('building_permit_filtered.json') as infile:
    all_status = [line.split(',')[13] for line in infile.readlines()]
with open('building_permit_filtered.json') as infile2:
    all_address = [line.strip().split(',')[14] for line in infile2.readlines()]
with open('building_permit_filtered.json') as lats:
    all_lats = [line.strip().split(',')[51] for line in lats.readlines()]
with open('building_permit_filtered.json') as longs:
    all_longs = [line.strip().split(',')[52] for line in longs.readlines()]
