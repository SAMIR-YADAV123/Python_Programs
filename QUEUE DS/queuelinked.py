class node:
   def __init__(self,data):
      self.data=data
      self.next=None

class queue:
    def __init__(self):
        self.f=None
        self.r=None

    def insert(self,x):
        newnode=node(x)
        newnode.next=None

        if self.r==None:
            self.r=self.f=newnode
        else:
            self.r.next=newnode
            self.r=self.r.next

    def insertsp(self,x,y):
        newnode=node(x)
        temp=self.f
        i=1
        while(i<y-1):
            temp=temp.next
            i+=1

        newnode.next=temp.next
        temp.next=newnode

    def delet(self):
        if self.f==None:
            print("Empty")
        elif self.f==self.r:
            self.f=self.r=None
        else:
            temp=self.f
            self.f=self.f.next
            del temp


    def show(self):
        if self.f==None:
            print("EMPTY")
        else:
          temp = self.f
          while(temp!=None):
             print(temp.data)
             temp=temp.next

obj=queue()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
#obj.delet()
#obj.delet()
#obj.insertsp(5,2)
obj.show()