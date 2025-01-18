
n= int(input("enter the number of rows"))
start=1

for i in range(1,n+1):
        if i % 2 == 0:  
            for j in range(start, start + i):
                print(j, end=" ")
        else:  
            for j in range(start + i - 1, start - 1, -1):
                print(j, end=" ")

        start += i  
        print()  
