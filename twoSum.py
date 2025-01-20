# Two sum:                                                                                                          
# Given an array of integers nums and an integer target, return the indices of the 
# two numbers such that they add up to target
# 123456   => 9
# Using hashing concept

def twoSum(arr,target):
    hashMap={}
    i = 0
    for num in arr:
        anotherNum = target - num
        if anotherNum in hashMap:
            return [hashMap[anotherNum],i]
        hashMap[num]=i
        i+=1
    return []

nums = list(map(int,input("enter the elements with spaces").split()))
target = int(input("enter the target"))
print(twoSum(nums, target))
        


