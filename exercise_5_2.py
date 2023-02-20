largest = (None)
smallest = (None)
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(n)
        if (largest is None):
            largest = n 
        if (n > largest):
            largest = n
        if (smallest is None):
            smallest = n
        if (n < smallest):
            smallest = n 
    except:
        print("Invalid input")
        continue 
print("Maximum" , largest)
print("minimum" , smallest)












'''largest = (None)
smallest = (None)
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)    
        if (largest is None):
            largest = n
        elif (largest < n): 
            largest = n  
        if (smallest is None):
            smallest = n
        elif (smallest > n):
            smallest = n 
    except:
        print("Invalid input")
        continue    
print("Maximum" , largest)
print("minimum" , smallest)

'''