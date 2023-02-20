import re
import urllib.request , urllib.parse, urllib.error
from bs4 import BeautifulSoup

count = int(input('enter a count: '))
position = int(input("enter position: "))
run = 0
url = input('enter a file name: ')
html = urllib.request.urlopen(url).read()
while count > run:

    soup = BeautifulSoup(html, 'html.parser')

    href = soup('a')
        #print('TAGS',name)
    for name in href:
        #print(name)
        #print('URL' , name.get('href' , None))

        lst = list()
        greet = 'URL:', name.get('href', None)        
        lst.append(greet)
        #print('LST',lst)   
        #print('LSTTTT333',lst[3])
        #for name in greet:
        #print('LST',lst[0])
        '''words = name.decode().split()
        #print("WORDS" , words)
        var = words[1]
        #print('PART' , var)
        #print('NAME' , var[45-50])
        greet = var.split('/')
        #print('GREET' , greet)
        take = greet[3]
        #print(take)
        like = take.split('_')                      
        #print(like)
        my = like[2]
        #print(my)
        your = my.split('.')
        #print(your)
        our = your[0]
        #print(our)
        lstt = list()
        lstt.append(our)'''
        #print(name)
        #print('LLLSSSSTTTT' , lstt)
    link = href[position].get('href' , None)
    linc = ('JAK',href[position].contents[0])
    print('GETTT',linc)
    run = run + 1
    print('RRRUUUNNN' , run)
    html = urllib.request.urlopen(link).read()
    #var = name.split()
    #print('VAR' , var)