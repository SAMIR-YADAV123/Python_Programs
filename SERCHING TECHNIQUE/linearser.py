def linearsearch(arr,n):
    x=int(input("enter the element which want to search:"))
    found=0
    for i in range(n):
        if arr[i]==x:
            found=i

    if found==0:
       print("element not found")
    else:
        print("element found at:",found+1)


print("Enter the array element:")
li=[int(x) for x in input().split()]
n=len(li)
linearsearch(li,n)