from geopy.geocoders import Nominatim
import json
from pprint import pprint
count=0
outfile = open('building_permit_cleaned_up.json','w')
list1=[]
with open('building_permit_clean.json','r') as building_json:
    data = json.load(building_json)
    for object1 in data:
        if(object1['status']==[]):
            print("EMPTY")
        if(object1['lats']==[]):
            print("EMPTY")
        if(object1['longs']==[]):
            print("EMPTY")
        else:
            if(object1['status'][0] != str(" \"Issued\"") and ( object1['status'][0] != str(" \"CO_Issued\""))):
                print("BAD")
                count+=1
            if((object1['lats'][0] == (" "+b'null')) or (object1['lats'][0] == str("\\\"zip\\\":\\\"\\\"}")) or (object1['lats'][0] == str("\\\"zip\\\":\\\"\\\"}\""))):
                print("BAD")
                count+=1
            if "-87" not in object1['longs'][0]:
                print("BAD")
                count+=1
                if((object1['longs'][0] == (" "+b'null'))or object1['longs'][0] == str(" null") or ( object1['longs'][0] == str(" null"))):
                    print("BAD")
                    count+=1

            else:
                print("GOOD")
                list1.append(object1)
    json.dump(list1, outfile)
    count=count+1
