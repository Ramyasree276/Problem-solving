# moore's voting algorithm

# majority element should be greater than n/2 where n is length of the array.

def majorityElement(arr):
    ele = 0
    count = 0
    for i in range(len(arr)):
        if(count==0):
            ele=arr[i]
            count+=1
        elif arr[i]== ele:
            count+=1
        else:
            count-=1
    cnt=0    
    for i in range(len(arr)):
        if arr[i] == ele:
            cnt+=1
    if(cnt >(len(arr)//2)):
        return ele
    return -1

arr= list(map(int,input("enter the elements with space").split()))
print(arr)
n = majorityElement(arr)
print("majority element is {}".format(n))