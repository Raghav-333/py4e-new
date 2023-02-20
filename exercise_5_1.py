#Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.






total = 0
count = 0
average = 0
     
while True:
    inp = input("Enter a number or done: ")
    if inp == ("done"):
        break
    try:
        n = int(inp)
        count = count + 1
        total = total + n 
        average = total / count 
    except:
        print("Invalid input")
        continue  
print("Count" , count)
print("Total" , total)
print("Average" , average)
