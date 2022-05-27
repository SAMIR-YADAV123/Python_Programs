def binarysearch(arr,n):
    x=int(input("enter which element wants to find:"))
    fo=0
    lb=0
    hb=n
    while lb<=hb:
        mid=int((lb+hb)/2)

        if arr[mid]==x:
            fo=mid+1
            break
        elif arr[mid]>x:
            hb=mid
        elif arr[mid]<x:
            lb=mid

    if fo==0:
        print("element not found:")
    else:
        print("Element found at:",fo)

print('enter the array eelement:')
li=[int(x) for x in input().split()]
n=len(li)
binarysearch(li,n)