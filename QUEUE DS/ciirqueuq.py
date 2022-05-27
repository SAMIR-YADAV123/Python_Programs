def insert():
   global f, r, arr, n
   if f==(r+1)%n:
       print("queue is full:")
   else:
       x=int(input("enter the element:"))
       if f==-1:
           f=r=0
       else:
           r=(r+1)%n

       arr[r]=x

def delet():
    global f, r, arr, n
    if f==-1:
        print("underflow:")
    else:
        arr[f]=None
        if f==r:
            f=r=-1
        else:
            f=(f+1)%n

    return

def display():
    global f,r,arr,n

    if r==-1:
        print("queue is empty:")
    else:
        print(arr)
        print("element of queue are :")
        for i in range(f,n):
         print(arr[i],end=' ')
        for i in range(r, f):
             print(arr[i], end=' ')

        print()




n=int(input("enter the size of c queue:"))
f=r=-1
arr=list(None for i in range(n))
print("menu:")
print("1.ENQUEUE","2.DEQUEUE","3.DISPLAY","4.EXIT")
while(1):
    ch=int(input("enter your choice:"))
    if ch==1:
        insert()
    elif ch==2:
        delet()
    elif ch==3:
        display()
    elif ch==4:
        exit(0)
    else:
        print("ente valid choice:")

