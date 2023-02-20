'''purse = dict()
purse['greet']  = 23
purse['candy'] = 75
purse['get'] = 3
print(purse) #printing the dictionary
print(purse['get']) #printing an specefic element in a dictionary
purse['candy'] = purse['candy'] + 2 #Manipulating a dictionary
print(purse['candy'])'''










'''name = dict()
name['csev'] = 1
name['cwen'] = 1
print(name)
name['csev'] = name['csev'] + 1
print(name)'''








'''count = dict()
var = ['csev' , 'cwen' , 'csev' , 'zqian' , 'cwen']
for i in var:
    if i not in count:
        count[i] = 1        # Count is empty there is atleast of the the values that we have in the dictionary so firstly it add 1 to the dictionary and if there is the value again in the list it runs the else code
    else:
      count[i] = count[i] + 1
print(count) ''' 










'''count = dict()
var = ['csev' , 'cwen' , 'csev' , 'zqian' , 'cwen']
for i in var:
    if i not in count:
        count[i] = 1        
    else:
      count[i] = count[i] + 1
print(count)
count.get(i,0)'''
#In this code we are using get() function only to get rid of the print statements again and again











'''count = dict()
var = ['csev' , 'cwen' , 'csev' , 'zqian' , 'cwen']
for name in var:
    count[name] = count.get(name,0) + 1
print(count)'''









'''counts = dict()
a = input('enter a file: ')
#hnad = open(a)
spl = a.split()
print(spl)

for words in spl:
    counts[words] = counts.get(words,0)+1
print(counts)'''









'''jjj = {'chuck' : 1 , "fred" : 42 , 'jan' : 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())'''









'''jjj = {'chuck' : 1 , "fred" : 42 , 'jan' : 100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)'''
#This program goes through all the items in the dictionary and aaa represents the keys and bbb represents the values.











'''fhand = input('enter a file: ')
fname = open(fhand)
counts = dict()

for line in fname:
    words = line.split()
    #print(words)
    for name in words:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
print(counts)

bigword = None
bigcount = None
for get,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = get  
        bigcount = count  
print(bigword , bigcount)'''