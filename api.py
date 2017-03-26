import json, urllib
from urllib import urlencode
import googlemaps
start = "San Diego, CA, United States"
finish = "Tuscaloosa, AL, United States"

gmaps = googlemaps.Client(key='AIzaSyBOs0PEEd5KAj7WQWv0a5CDFmQcoqNfZhY')
directions = gmaps.directions(start,finish,alternatives=True)

print directions["Directions"][0]["Distance"][0]["meters"]
import json, urllib
from urllib import urlencode
import googlemaps
start = "Bridgewater, Sa, Australia"
finish = "Stirling, SA, Australia"

url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode(('origin', start),('destination', finish)))
ur = urllib.urlopen(url)
result = json.load(ur)

for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
                                 print j
