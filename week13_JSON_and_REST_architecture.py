"""import json 

stuff = '''
{
    "name" : "chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
    "email" : {
        "hide" : "yes"
    }       
}
'''

info = json.loads(stuff)
#print('name: ' , info["name"])
#print('Hide:' , info["email"]["hide"])"""












"""import json
input = '''
[
    { "id" : "001",
      "x" : "2",
      "name" : "chuck"
    },
    { "id" : "009",
      "x" : "7",
      "name" : "Chuck"
    }
]'''

info = json.loads(input)
#print('length' , len(info))

for item in info:
    #print('id', item['id']) 
    #print('name' , item['name'])        
    #print('attr' , item['x'])"""













'''import urllib.request , urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('enter a location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    #print('Retrieving: ' , url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    #print('Retrieved' , len(data) , 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        #print('====FAILURE TO RETRIEVE====')
        ##print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    
    #print('lat:',lat , 'lng' , lng) 
    location = js['results'][0]['formatted_address']
    #print(location)'''










    
 
"""import json
import urllib.request , urllib.parse, urllib.error
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    acct = input('enter twitter account: ')
    if len(acct) < 1:break
    url = twurl.augment(TWITTER_URL,{'screen_name' : acct, 'count' : '5'})

    #print('retrieving' , url)
    connection = urllib.request.urlopen(acct)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    #print('Remaining', headers['x-rate-limit-remaining'])

    js = json.loads(data)  
    #print(json.dumps(js, indent=4))

    for u in js['users']:
        #print(u['screen_name'])
        s = u['status']['text']
        #print('    ' , s[:50])"""













import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    #print('GETITITITI: ',parms)
    url = serviceurl + urllib.parse.urlencode(parms)

    #print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        #print('==== Failure To Retrieve ====')
        #print(data)
        continue

    #print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    #print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    #print(location)