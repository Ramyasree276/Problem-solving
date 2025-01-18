def intersection(arr1,arr2):
    set1= set(arr1)
    set2=set(arr2)
    inter = set1.intersection(set2)
    return inter

arr1 = list(map(int,input("enter the values with spaces").split()))
arr2 = list(map(int,input("enter the second array values with spaces").split()))
intersection_array=intersection(arr1,arr2)
print(intersection_array)