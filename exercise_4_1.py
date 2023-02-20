def computepay(h, r):
    return (h*r)

hrs = float(input("Enter Hours:"))
rate = float(input("enter rate:"))
if hrs > 40:
    a = computepay(hrs,rate)
    b = hrs - 40
    c = b*0.5*rate
    final = (c+a)
    print("Pay" , final)
else:
    one = computepay(hrs*rate)
    print("Pay" , one)
