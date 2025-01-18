def binary(low,high,arr1,x):
    arr= arr1
    while(low<=high):
        mid = low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1

x= 20 
arr1= list(map(int,input("enter numbers with space").split()))
# arr1=[1,13,20,34,45,56,67,78]
result= binary(0,len(arr1),arr1,x)
print(result)
        