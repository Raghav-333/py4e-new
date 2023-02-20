hrs = input("Enter Hours:")
rate = input("Enter Rate per hour:")
h = float(hrs)
r = float(rate)
if (h <= 40):
    start = h*r
    print(start)
elif (h > 40):
    start = 40*r
    sub = h - 40
    end = r*1.5*sub
    add = start+end
    print(add)

