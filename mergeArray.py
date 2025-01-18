# merging two sorted arrays
n= int(input("enter the number of elements in sorted array"))
arr1=[]
arr2=[]
for i in range(n):
    num = int(input("enter the value"))
    arr1.append(num)
m= int(input("enter the elemets of the second sorted array"))
arr2 = list(map(int,input(f"enter {m} values of the array with space").split()))
merged=[]
i=0
j=0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1
while(i< n):
    merged.append(arr1[i])
    i+=1
while(j< m):
    merged.append(arr2[j])
    j+=1

print(merged)
