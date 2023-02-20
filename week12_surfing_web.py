# The ord function returns the ASCII value for a string or a sign or a number.
'''print(ord('H')) #Capital letter H
print(ord('e')) #Small letter e
print(ord('\n'))''' #Newline 









'''a = b'abc'
print(type(a))
b = 'abc'
print(type(b))
c = u'abc'
print(type(c))'''











'''import urllib.request , urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# print(fhand)
for line in fhand:
    print(line)
    print(line.decode().strip())'''
    
# decode() fuction creates byte type into string type













'''import urllib.request , urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhand:
    words = (line.decode().strip())
    for word in words:
        if word == ' ':
            continue 
        count[word] = count.get(word , 0) + 1
print(count.items())
bigword = None
bigcount = None

for get , count in count.items():
    if bigcount is None or count > bigcount:
        bigword = get
        bigcount = count'''
#print(bigword , bigcount)













'''import urllib.request , urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())'''










'''import urllib.request , urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    # print(line)
    words = line.decode().split()
    # print(words)
    for word in words:
        counts[word] = counts.get(word , 0) + 1  # passing 0 in '(word , 1)' as the default value
        # print(counts.get(word))
print(counts)

# Extracting the word and their counts from a file from the internet
# 'get' Return the value for key if key is in the dictionary, else default'''











'''import urllib.request , urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())'''
#Returns the HTML code for a website using urllib










 
'''import urllib.request , urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('enter-')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)'''