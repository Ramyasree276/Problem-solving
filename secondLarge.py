arr= list(map(int,input("enter values with space").split()))
# i = 0
# j= len(arr)
maxi=0
secmax=0
for i in range(len(arr)):
    if(arr[i]>maxi):
        secmax=maxi
        maxi=arr[i]
    elif(arr[i]<maxi and arr[i]>secmax):
        secmax=arr[i]
print(secmax)


