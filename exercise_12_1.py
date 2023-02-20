import re
import urllib.request , urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('enter a file name: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)