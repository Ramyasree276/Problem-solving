def computeGCD(x,y):
    while(y):
        x,y=y,(x%y)
    return x


n= int(input("enter number"))
m= int(input("enter number"))
print(f"GCD of {n} and {m} is ",computeGCD(n,m))
lcm = n*m // computeGCD(n,m)
print("LCM of {} and {} is {}".format(n,m,lcm))