n = int(input("enter the no of values in the series"))
a = 1
b=1
c=2
for i in range(n):
    c =b+c
    b=c-b
    print(c,end=" ")
# n = int(input("enter the max value in the series"))
# while(c<n):
#     c =b+c
#     b= c-b
#     print(c,end=" ")