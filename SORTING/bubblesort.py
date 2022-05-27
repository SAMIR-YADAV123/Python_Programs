def bubble(arr,n):
   for i in range(n):
      for j in range(0,n-i-1):
          if arr[j]>arr[j+1]:
              arr[j],arr[j+1]=arr[j+1],arr[j]
   for i in range(n):
      print(arr[i],end=" ")

print("enter the array element:")
li=[int(x) for x in input().split()]
n=len(li)
bubble(li,n)