#WAP to enter P R T and return amt 

def amount():
    p = int(input("Enter principle amount = "))
    r = float(input("Enter the rate of interest = "))
    t = int(input("Enter time in yrs = "))
    si = (p*r*t)/100
    amt = p + si
    return amt , si
x,y = amount()
print("Total Payable amount = ",x)
print("Total Interest = ",y)

