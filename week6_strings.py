'''fruit = ("banana")
number = fruit[1]
print(number)'''




'''var = ("banana")
index = 3
w = var[index - 1]
print(w)'''
#in here if index in typed in line 10 then it will print 'a'





'''fruit = ('banana')
print(len(fruit))'''
#the len function returns us the length of the string






'''fruit = ('banana')
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter , index)
    index = index + 1'''
#prints the index of the word simultaneously






'''fruit = ("banana")
for letter in fruit:
    print(letter)'''
#it is better to use for loop instead of while loop





'''count = ("banana")
num = 0
for letter in count:
    if letter == 'a':
        num = num + 1
print(num)'''
#this program counts the no. of a in the string






'''s = ("monty python")
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:])
print([:7])
print([3:])''' 
#it is called slicing
#we would go up to the end but not including it







'''a = ('hello')
b = a + 'mosh'
print(b)'''





'''a = "hello"
b = a + ' ' + "mosh"
print(b)'''
#string concatenation






'''fruit = ('banana ')
a = ('n') in fruit 
b = ('nan') in fruit 
c = ('m') in fruit 
d = (' ') in fruit 
print(a)
print(b)
print(c)
print(d)
if 'a' in fruit:
    print('found it')'''
#using in as a logical operator






'''word = input("enter a word : ")
if word == 'banana':
    print('all right, bananas ')
if word > "banana":
    print('your word ' + word + ' comes before banana')
elif word < "banana":
    print('your word ' + word + ' comes after banana')
else:
    print("all right , bananas")'''
#string comparison






'''var = "Hello Bob"
a = var.lower()
print(a)
print(a.upper())
print('hello there'.upper())'''
# .lower() minimize all the letters in a string 
# .upper() capitalize all the letters in a string







'''stuff = 'hello'
a = type(stuff)
print(a)
b = dir(stuff)
print(b)'''
#dir stands for directory






'''fruit = 'banana'
a = fruit.find("na")
print(a)'''
# find operator is just same as in but instead of returning true/false it returns the place where it founds it








'''var = 'hello bob'
nstr = var.replace('bob' , 'jane')
print(nstr)'''
#the replace function will replace all the occurance of the first string with the second string







'''greet = 'Please have a nice day'
x = greet.startswith('Please')
y = greet.startswith('p')
print(x)
print(y)''' 
#startswith function returns the prefix as true or false





'''data = 'From john.amber@uct.ac.za Sat'
atpos = data.find('@')
print(atpos)
var = data.find(' ' ,atpos)
print(var)
sppos = data[atpos+1 : var]
print(sppos)'''
#finding a section of a string using slicing and find operator







'''greet = '       hello bob       '
a = greet.lstrip()
b = greet.rstrip()
c = greet.strip()
print(a)
print(b)
print(c)'''
#rstrip() and lstrip() removes whitespaces from both left and right
#strip() removes whitespaces from both beginning and ending