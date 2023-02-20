'''a = input('enter ')
fh = open(a)
fh = fh.read()
b = fh.find('X-DSPAM-Confidence:')
print(b)'''





a = input('enter: ')
fh = open(a)

count2 = 0
zork2 = float(0)
for lin in fh:
    if not lin.startswith("X-DSPAM-Confidence:"):
        continue
    line = lin.strip()
    count2 = count2 + 1
    #print('count2', count2)
    #print(line)
    valu = (line[19:])#0.9876
    value = float(valu)
    #print('valu',value)
    zork2 = zork2 + value
    #print('zork2',zork2) 
    #print('vlaue',value)
    #print(type(value))
    #zero = 0


'''zork = float(0)
for num in value:
    zork = zork + float(num)
    print('zork',zork) '''
div = zork2/count2 
print('ans',div)


















































'''a = input('enter ')
fh = open(a)
fh = fh.read()
b = fh.find('X-DSPAM-Confidence:')
print(b)'''





'''a = input('enter: ')
fh = open(a)

for lin in fh:
    if not lin.startswith("X-DSPAM-Confidence:"):
        continue
    line = lin.rstrip()
    print(line)
    valu = (line[19:])
    value = float(valu)
    print('vlaue',value)
    print(type(value))
    #zero = 0
  
    
    var = sum(value) 
    print('su',var)'''
'''zer = 0
for ran in range(value):
    zero = zer + value
    print('zero', zero)'''
'''count = 0 
for value in line:
    #value = float(value)
#print(value)
    count = count + 1 #number
print('cou',count)
zork = float(0)
for num in value:
    zork = float(zork) + float(value) 
    
#print(count)

 

div = zork/count
print('ans',div)
#cun = sum(value)
d = value.count()
print(d)'''






'''zork = 0
print('before' , zork)
for num in [9, 21, 12, 45, 9, 74, 15]:
    zork = zork + num
    print(zork)
print("after" , zork)'''
