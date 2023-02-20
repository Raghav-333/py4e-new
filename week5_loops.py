'''n = 5
while (n > 0):
    print(n)
    n = n - 1
print("blastoff")
print(n)'''







'''n = 5
while n > 0:
    print("lather")
    print("rinse")
print("Dry off")'''  #this is an infinite loop







'''n = 0
while n > 0:
    print("lather")
    print("rinse")
print("dry off")'''#This is a zero trip loop








'''while True:
    line = input("> ")
    if line == ("done"):
        break
    print(line)
print("Done!")'''
#In the above loop when "done" is typed it will break otherwise line will be printed







'''while True:
    line = input("> ")
    if line[0] == ("#"):
        continue
    if line == ("done"):
        break
    print(line)
print("Done!")'''
# When index[0] is a '#' sign the program will not run and it get back to the top and run the 1st statement










'''for i in [5, 4, 3, 2, 1]:
    print(i)
print("blastoff")'''






'''friends = ['Joseph' , 'Glenn' , 'Sally']
for new in friends:
    print("happy new year" , new)
print("Done!")'''








#largest number finder
'''largest_so_far = (-1)
print("Before" , largest_so_far)
for the_num in [9, 21, 12, 45, 9, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(the_num , largest_so_far)
print("after" , largest_so_far)'''









# Counting how many numbers
'''zork = 0
print("before" , zork)
for num in [9, 21, 12, 45, 9, 74, 15]:
    zork = zork + 1
    print(zork , ':' , num)
print("after" , zork)'''







# Finding the total
'''zork = 0
print('before' , zork)
for num in [9, 21, 12, 45, 9, 74, 15]:
    zork = zork + num
    print(zork)
print("after" , zork)'''









# Average = sum/count
'''sum = 0
count = 0
print('Before' , sum , count)
for zork in [9, 21, 12, 45, 9, 74, 15]:
    sum = sum + zork
    count = count + 1
    print(sum , count, zork)
print(sum , count , sum/count)''' # This program is very important










'''print("before")
for count in [9, 21, 12, 45, 74, 15]:
    if (count > 20):
        print("Large Number" , count)
print("After")'''    # Large number finder








# Search using a boolean variable
'''found = False
for value in [9, 21, 12, 45, 74, 15]:
    if value == 45:
        found = True 
    print(found , value)
print("After" , found)'''
# After found turns true all the other values will also turn true











# Smallest number finder
'''smallest = None
print("Before")
for value in [9, 21, 12, 45, 3, 74, 15]:
    if (smallest is None):
        smallest = value
    if (value < smallest):
        smallest = value
    print(smallest , value)
print("After" , smallest)'''



