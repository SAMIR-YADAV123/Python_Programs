class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class cirlinked:
    def __init__(self):
        self.head=None

    def inesertlist(self,x):
        newnode=node(x)
        if self.head==None:
            self.head=newnode
            newnode.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            newnode.next=self.head
            temp.next=newnode
            self.head=newnode

    def addatend(self,x):
        temp=self.head
        newnode=node(x)
        while temp.next!=self.head:
            temp=temp.next
        newnode.next=self.head
        temp.next=newnode
        self.head=newnode
    def addatsp(self,x,y):
        newnode=node(x)
        temp=self.head
        i=1
        while(i<y-1):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode


    def serchnode(self,x):
        temp=self.head
        while temp.next!=self.head:
            if temp.data==x:
                print("data found:")
                return
            else:
                temp=temp.next
        if temp==self.head:
            print("not found:")
    def deletenode(self,x):
        temp=self.head
        prev=None
        while temp.next!=self.head and temp.data!=x:
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp=temp.next
    def display(self):
        print("element are:")
        temp=self.head
        while temp.next!=self.head:
            print(temp.data)
            temp=temp.next
        print(temp.data)
obj=cirlinked()
obj.inesertlist(2)
obj.inesertlist(4)
obj.inesertlist(6)
#obj.display()
obj.addatend(5)
#obj.display()
obj.serchnode(4)
#obj.display()
obj.addatsp(3,2)
obj.display()
obj.deletenode(6)
obj.display()