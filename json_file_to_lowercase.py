import json
from pprint import pprint

with open('building_permit_cleaned_up.json') as data_file:    
    data = json.load(data_file)

for c in range(0,len(data)):
	pprint(data[c]["address"][0].lower())

