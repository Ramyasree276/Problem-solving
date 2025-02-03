def longSub(str):
    left = 0 
    max_len=0
    hashSet=set()
    for right in range(len(str)):
        while str[right] in hashSet:
            hashSet.remove(str[left])
            left +=1
        hashSet.add(str[right])
        max_len=max(max_len,right-left+1)
    return max_len

str = input("enter a string")
print(longSub(str))

