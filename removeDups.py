arr = list(map(int,input("enter the values of array with space").split()))
# for i in arr:
#     print(i,end=" ")
print(arr)
print("Using set()")
arr1=set(arr)
print(list(arr1))
index=1
print("Without using set() for sorted array")
i=0
for j in range(1,len(arr)):
    if(arr[i]!=arr[j]):
        arr[i+1]=arr[j]
        i+=1
        index+=1
    
for j in range(index):
    print(arr[j], end=" ")
        
print(arr)
print("Number of unique elements are:",index)

