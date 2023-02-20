'''handle = open('python.txt' , 'r')
print(handle)'''
#open() function opens the file 
#open() function has two modes 'r' to read the file and 'w' to write in the file







'''handle = open('stuff.txt' , 'r')
print(handle)'''
#If you try to open a file that doesn't exist you would get a traceback 







'''stuff = ("hello\nworld")
print(stuff)
var = 'X\nY'
print(var)
a = len(var)
print(a)'''
#the newline method is counted as one character






'''handle = open('python.txt')
for cheese in handle:
    print(cheese)'''
#by using a for loop we can read through the file 







'''fhand = open('python.txt')
print(fhand)
count = 0
for line in len(fhand):
    count = count + 1
print(count)'''
#this program counts the number of lines in a file







'''var = open('python.txt' , 'r')
var = var.read()
b = len(var)
print(b)
print(var[:20])'''
#This program tells us the number of characters in a file
#We will have to use the read() function to get the number of characters








'''fhand = open('python.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)'''
#var fhand is only used for opening the file and the variable line first loop through the file and the find the lines starting with From: and then prints them
#you will get blank lines in the output because print statement 







'''fhand = open('python.txt')
for line in fhand:
    if line.startswith('From: '):
        line = line.rstrip()
        print(line)'''
#We will use the rstrip method to get rid of the blank lines in the output.







'''fhand = open('python.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)'''
#We can also write the program with a different logic with the help of not statement
    







'''fhand = open('python.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)'''
#In this program we find the statement we want.









fname = input('enter a file:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject: '):
        print(line)
        count = count + 1
print('There were' , count , 'Subject lines in' , fname )
#In this program we take the file as an input and count the number of lines starting with the string








'''fname = input('enter a file:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened' , fname)
    quit()
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject: '):
        count = count + 1
print('There were' , count , 'Subject lines in' , fname )'''
#If the user types an invalid file name the program will give an error using try and except statements
