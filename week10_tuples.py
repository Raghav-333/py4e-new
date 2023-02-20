'''a = ('glenn' , 'sally' , 'joseph')
print('a',a[2])
b = (1 , 9 , 2)
print('b',b)
print('c',max(b))
for iter in b:
    print('d',iter)'''








'''(x , y) = (4 , 'fred')
print(y)''' #If we put two variables in a tuple and it will take the value on the right or the left side










#Tuple comparision
'''a = (4 , 8 , 6) > (2 , 5 , 9)
print(a)
b = (2 , 8 , 200000) < (5 , 9 , 2)
print(b)
c = ('jones', 'sally') < ('jones' , 'sam')
print(c)'''
#For comparision it goes from left to right and if the first digit is equal then it only moves on to the next digit
#For string comparision it checks the words in alphabetical order









'''d = {'a':10 , 'b': 11 , 'c':9 , 'ghg':77}
a = d.items()
print(a)
b = sorted(d.items())
print(b)'''
#We can form a dictionary and then sort it with the help of sorted function of tuples










'''d = {'u':10 , 'e': 11 , 'h':9}
b = sorted(d.items())
print(b)
for k,v in sorted(d.items()):
    print(k,v)'''









'''d = {'u':74 , 'j':88 , 'a':9}
lst = list()
for k,v in d.items():
    lst.append((v , k))
print(lst)
a = sorted(lst)
print(a)'''












'''from audioop import reverse

a = input('enter a file: ')
op = open(a)
counts = dict()
for var in op:
    itr = var.split()
    for name in itr:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
#print(counts)

lst = list()
for key,value in counts.items():
    newtup = (value , key)
    lst.append(newtup)
lst = sorted(lst , reverse=True)

for value,key in lst[:10]:
    print(value,key)'''










'''c = {'y':3 , 'k':9 , 'a':99}
print(sorted([(v,k) for k,v in c.items()]))'''
# Dynamaic List Comprehension




























a = input('enter a file: ')
fhand = open(a)
counts = dict()
for name in fhand:
    if name.startswith('From '):
        fname = name.rstrip()
        fname = name.split()
        #print('a' , fname)
        itr = fname[5]
        #print('itr' , itr)
        var = itr.split(':')
        itre = var[0]
        #print(itre)
        if itre not in counts:
            counts[itre] = 1
        else:
            counts[itre] = counts[itre] + 1
#print(counts)
lst = list()
for key,value in counts.items():
    newtup = (key,value)
    lst.append(newtup)
lst = sorted(lst)
for key,value in lst:
    print(key,value)
