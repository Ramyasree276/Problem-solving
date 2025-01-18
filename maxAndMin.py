arr = list(map(int,input("enter the array values").split()))
n = len(arr)
mini = arr[0]
maxi = arr[0]
for i in range(n):
    if(arr[i]<=mini):
        mini=arr[i]
    elif(arr[i]>=maxi):
        maxi= arr[i]

print(f"minimum {mini} and maximum {maxi}")
