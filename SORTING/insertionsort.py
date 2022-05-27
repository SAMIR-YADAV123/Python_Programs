def insertion(arr,n):
    for i in range(1,n):
        tem=arr[i]
        pos=i
        while tem>arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1

        arr[pos]=tem

    for i in range(n):
        print(arr[i], end=" ")





print("enter the array element:")
li=[int(x) for x in input().split()]
n=len(li)
insertion(li,n)