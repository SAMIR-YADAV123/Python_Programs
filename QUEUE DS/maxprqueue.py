def insert():
     x = int(input("enter the element:"))
     global f, r, arr, n
     if r==3:
         print("queue is full:")
     else:
         if f==-1:
             f=r=0
             arr[r]=x
         else:
             t=0
             for i in range(0,r+1):
                 if x >= arr[i]:
                     for j in range(r+1,0,-1):
                         arr[j]=arr[j-1]
                     arr[i]=x
                     r+=1
                     t=1
                     break


             if t==0:
                 r+=1
                 arr[r]=x

def delet():
    global f, r, arr, n
    if f==-1:
        print("underflow:")
    elif f==r:
        arr[f]=None
        f=r=-1
    else:
        arr[f]=None
        f+=1

def display():
    global f,r,arr,n

    if r==-1:
        print("queue is empty:")
    else:

        print("element of queue are :",arr)



n=4
f = r =- 1
arr=list(None for i in range(4))
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
