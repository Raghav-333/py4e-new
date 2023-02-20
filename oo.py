# PROGRAM TO FIND PERFECT SQUARED TILL A GIVEN LIMIT


z = int(input("Enter a Value: "))
def sqrt(a):
    
    for i in range(1,999999999999999999):
        x = (i*i)
        if x<=a:
            #print(x)
            z = x ** 0.5
            print(int(z))
sqrt(z)
