import re

handle = open('regex.txt')
num = 0
for line in handle:
    stuff = re.findall('[0-9]+' , line)
    for plus in stuff:
        num = num + int(plus)
print(num)