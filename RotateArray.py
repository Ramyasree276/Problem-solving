def rotate(arr,k):
    n= len(arr)
    k= k%n
    def reverse(low,high):
        while low<high:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1

    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
k = int(input("enter the no of rotations"))
arr = [1,2,3,4,5,6,7]
rotate(arr,k)
print(arr)