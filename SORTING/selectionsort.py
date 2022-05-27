def selection(arr,n):

    for i in range(n):
        pos=-1
        small=arr[i]
        for j in range(i+1,n):
            if small>arr[j]:
                small=arr[j]
                pos=j

        if pos!=-1:
            temp=arr[i]
            arr[i]=arr[pos]
            arr[pos]=temp

    print("Sorted element are:",arr)

print('enter the array eelement:')
li=[int(x) for x in input().split()]
n=len(li)
selection(li,n)