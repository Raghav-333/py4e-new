#a list is anything in square brackets




'''print([1 , 1.2 , 87])#a list of integers
print(['red' , 'yellow' , 'blue'])#a list of strings
print('red' , 24 , 98.6)#a list of integers cum strings
print(1 , [5 , 6] , 7)#a list within a list
print([])'''#an empty list








'''a = ['Joseph' , 'Glenn' , 'Sally']
for friend in a:
    print('Happy New Year' , friend)
print('Done!')'''
#Using in operator in a list








'''friend = ['Joseph' , 'Glenn' , 'Sally']
a = friend[1]
print(a)'''
#Using index operator in strings







'''num = [2 , 14 , 26, 64 , 72]
num[2] = 54
print(num)'''
#This shows us that lists are mutable
#In line 44 we don't need to assign a variable to mutate lists






'''x = [1 , 87 , 'joe' , 97]
print(len(x))'''








'''x = [1 , 87 , 'joe' , 97]
print(range(len(4)))'''
#Using range function in a list







'''friend = ['Joseph' , 'Glenn' , 'Sally']
for i in range(len(friend)):
    x = friend[i]
    print(x)'''







'''a = [1 , 2 , 3]
b = [4 , 5 , 6]
c = a + b
print(c)'''
#Concatenating strings 






'''t = [1 , 2 , 3 , 4 , 5 , 6]
print(t[2:4])
print(t[4:])
print(t[:4])
print(t[:])'''
#string slicing









'''stuff = list()
stuff.append('book')
stuff.append(18)
stuff.append('greet')
print(stuff)'''
#We can create an empty list and then add other elements in it
#Append() function is used to add an element to the last of the string








'''some = [1 ,  9 , 21 , 10 , 16]
a = 9 in some
print(a)
b = 18 in some
print(b)
c = 20 not in some
print(c)'''
#Using in operator to find something in a list







'''friend = ['Joseph' , 'Glenn' , 'Sally']
friend.sort()
print(friend)
print(friend[1])'''
#Sort method arranges a list in the alphabatical order







'''some = [1 ,  9 , 21 , 10 , 16]
print(len(some))#Length of the list
print(max(some))#Biggest number in the list
print(min(some))#Smallesst number in the list
print(sum(some))#Sum of all the numbers in the list
print(sum(some)/(len(some)))#Average of the list'''







'''numlist = list()
while True:
    a = input('Enter a Number:')
    if a == 'done':
        break
    num = float(a)
    numlist.append(num)
    plus = sum(numlist)
    count = len(numlist)
print(numlist)
average = plus/count
print('average',average)'''
#This program finds the average of the list









'''abc = 'With Three Words'
a = abc.split()
print(a)
print(len(a))
print(a[0])'''
#Split() function breaks a string to parts and produce lists






'''line = 'a lot           of spaces'
a = line.split()
print(a)

thing = ('first;second;third')
b = thing.split()
print(b)
print(len(b))

c = thing.split(';')
print(c)
print(len(c))'''









'''fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    spl = line.split()
    print(spl[2])'''








'''fhand = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = fhand.split()
print('1',words[1])
pieces = fhand.split('@')
print('2',pieces[1])'''