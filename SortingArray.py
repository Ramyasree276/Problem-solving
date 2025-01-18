def sorted(arr,n):
    for i in range(n):
        for j in range(0,n-i-1,1):
            if(arr[j]>arr[j+1]):
                # temp= arr[j]
                # arr[j]=arr[j+1]
                # arr[j+i]= temp
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


n = int(input("enter the number of elements of the array"))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
li = sorted(arr,n)
for i in li:
    print(i , end=" ")