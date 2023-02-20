import urllib.request , urllib.parse, urllib.error
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


address = input('enter a address: ')
parms = dict()
parms['address'] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('retrieving' , url)
print(parms)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print(data)
print('retrieved' , len(data) , 'characters')
try:
    js = json.loads(data)
except:
    js = None
if not js or 'results' not in js:
    print('======= SYSTEM FAILURE =======')
    print(data)


for item in js["results"]:
    place = item["place_id"]
    print('PLACE', place)