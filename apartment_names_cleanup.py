# @Author: Miclain K <user>
# @Date:   03-25-2017
# @Last modified by:   user
# @Last modified time: 03-25-2017


from geopy.geocoders import Nominatim
import json
from pprint import pprint

clean = open("complex_names_cleaned.txt", 'w')


with open('complex_names.txt') as infile:
    lines = infile.readline()
    count = True
    for line in infile:
        print(line)
        count = not count
        if count:
            clean.write(line)
