n = int(input("enter a number"))
# fac=1
# for i in range(1,n+1):
#     fac=fac*i
# print(fac)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
fac= factorial(n)
print(f"factorial of {n} is ",fac)