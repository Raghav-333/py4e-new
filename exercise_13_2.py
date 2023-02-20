import urllib.request , urllib.parse , urllib.error
import json

address = input('enter an url: ')
   
url = urllib.request.urlopen(address)
data = url.read().decode()

js = json.loads(data)


if not js or 'comments' not in js:
    print('======= SYSTEM FAILURE ========')
    print(data)

sum = 0
count = 0
for item in js["comments"]:
    #print(item)
    a = item["count"]
    #print(a)
    sum = sum + a 
    count = count + 1
print('SUM' , sum)
print('COUNT' , count)