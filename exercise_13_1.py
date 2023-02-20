import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')


uh = urllib.request.urlopen(address, context=ctx)
#data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
sum = 0
for item in lst:
    a = item.find('count').text
    print('get',a)
    #for var in a:
    sum = sum + int(a) 
    print(sum)
    #print(a)
print('done')


