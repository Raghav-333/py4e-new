'''search() method is able to find a pattern from any position of the string. The re.findall() helps to get a list of all matching patterns. It searches from start or end of the given string'''










'''import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From: ' , line):
        print(line)'''
# re stands for regular expression
# re.search without any special character is same as find method
# re.search find what to look for in the 1st parameter and where to look for in the 2nd parameter








'''import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ' , line):
        print(line)'''
# ^ before any word means the startswith fuction
# ^ matches the beginning of a line









'''import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:' , line):
        print(line)'''
# The dot(.) character matches any character
# The asterisk(*) character means any character 0 or more times
# In this code the colon(:) means the line should end with a colon()








'''import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:' , line):
        print(line)'''
# In this code 'X-' means startswith 'X-' 
# In this code '+' means repeats a character one or more number of times
# In this code '\S' means any non whitespace('space') character till the colon(:)











'''import re
x = 'My 2 favourite favor numbers are 9 and 42'
y = re.findall('[0-9]+' , x)
print(y)'''
# re.findall() returns a matching string containing all the matches
# In this code '[0,9]+' means that this code finds all the values starting from 0-9(0,1,2,3,4,5,6,7,8,9) in string x
# In this code '+' means that it can take more than one value that is a 2-digit-number or a 3-digit-number












'''import re
x = 'My 2 favourite favor numbers are 9 and 42'
y = re.findall('[AEIOU]+' , x)
print(y)'''










'''import re
x = 'From: Using the  : character'
y = re.findall('^F.+:' , x)
print(y)'''
# A greedy code
# A greedy code takes a big value 









'''import re
x = 'From: Using the  : character'
y = re.findall('^F.+?:' , x)
print(y)'''
# a non-greedy code
# A non-greedy code it takes a small value
# +? means one or more character but non-greedy









'''import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+' , x)
print(y)'''
# Any non-white space character one or more times then an @ sign and then any non-white space character one or more times
# If it founds any white space character then it terminates











'''import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)' , x)
print(y)'''
#Parentheses are not part of the match - but they tell where to start and stop what string to extract
# In this code if the string starts with 'From ' and satisfies the code in the parentheses













'''import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('(@[^ ]*)' , x)
print(y)'''
# In this code [^ ] return a match for any character except space
# The regex version












'''import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', x)
print(y)'''














'''`import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)' , line)
    if len(stuff) != 1 : continue
    get = float(stuff[0])
    numlist.append(get)
print(max(numlist))'''
#[0-9.] means any decimal number with the integer part being 0-9(0,1,2,3,4,5,6,7,8,9) and then having a decimal part
