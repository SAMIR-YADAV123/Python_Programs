class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    def insertion(self,x):
        newnode=node(x)
        newnode.next=None
        if self.top==None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode

    def insersp(self,x,y):
        newnode=node(x)
        newnode.next=None
        temp=self.top
        i=1
        while (i<y-1):
            temp=temp.next
            i+=1

        newnode.next=temp.next
        temp.next=newnode



    def delet(self):
        if self.top==None:
            print("underflow")
        else:
            temp=self.top
            self.top=self.top.next
            del temp

    def show(self):
        if self.top==None:
            print("underflow")
        else:
            temp=self.top
            while(temp!=None):
                print(temp.data)
                temp=temp.next

obj=stack()
obj.insertion(2)
obj.insertion(4)
obj.insertion(6)
obj.insertion(8)
#bj.delet()
obj.delet()
obj.insersp(3,1)
obj.show()