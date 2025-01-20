# 7 1 2 6 4 3
# cost = arr[i] - mini
# profit= max(cost,profit)
# mini=min(min,i)


def buyAndSell(arr):
    minprice=float('inf')
    maxpro=0
    for i in range(len(arr)):
        minprice=min(arr[i],minprice)
        maxpro=max(maxpro, arr[i]- minprice)
    return maxpro
arr=[7,1,2,1,2,3,2]
profit=buyAndSell(arr)
print(profit)
