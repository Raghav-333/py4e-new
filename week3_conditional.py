'''con1 = 5
if con1 < 10:
    print("smaller")
if con1 > 10:
    print("bigger")'''


'''x = 6
print("before 5")
if x == 5:
    print("is 5") 
    print("is still 5")
    print("third 5")
print("after 5")
print("before 6")
if x == 6:
    print("is 6")
    print("is still 6")
    print("third 6")
print("after 6")'''



'''x = 42
if x > 1:
    print("greater than 1")
    if x < 100:
        print("But Smaller than 100")
print("done")'''





'''astr = ('hello bob')
try:
    istr = int(astr)
except:
    istr = -1
print("first" , istr)'''




'''astr = ('123')
try:
    istr = int(astr)
except:
    istr = -1
print("second" , istr)'''



'''astr = ("bob")
try:
    print("hello")
    istr = int(astr)
    print("there")
except:
    istr = -1
print("done" , istr)'''
# In the above program , print("there") won't run because the program blows up on line 57 that is "istr = int(astr)"






'''rawstr = input("enter a number ")
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print("nice work")
else:
    print("not a number")'''