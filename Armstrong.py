n= int(input("enter the number"))
temp=n
res=0
ams=0
while(n>0):
    res=n%10
    ams=ams+res**3
    n=n//10
if(ams==temp):
    print("Armstrong number")
else:
    print("NOt Armstrong number")