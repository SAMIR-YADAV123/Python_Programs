class node:
    def __init__(self, data):
       self.data=data
       self.next=None
class singlink:
    def __init__(self):
      self.head=None

    def insertion(self,x):
        newnode=node(x)
        newnode.next=None
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def insertend(self,s):
        new_node=node(s)
        if self.head is None:
            self.head=new_node
        else:
            tem=self.head
            while tem.next is not None:
              tem= tem.next
            tem.next =new_node

    def insertatsp(self,x,y):
        newnode=node(x)
        temp =self.head
        I = 1
        while (I < y-1):
            temp = temp.next
            I = I + 1

        newnode.next = temp.next
        temp.next = newnode

    def delnode(self,x):
        temp=self.head
        if temp.data==x:
            self.head=temp.next
            return
        prev=None
        while temp.data !=x:
            prev=temp
            temp=temp.next
        if temp is None:
            return
        prev.next=temp.next

    def search_node(self,x):
        temp=self.head
        while temp is not None:
            if temp.data==x:
                print("element "
                      "matched:\n")
                return
            else:
                temp=temp.next
        if(temp==None):
            print("element not matched:")

    def reverse_linst(self):
        currentnode=self.head
        nextnode=None
        prevnode=None
        while(currentnode!=None):
          nextnode = currentnode.next
          currentnode.next = prevnode
          prevnode= currentnode
          currentnode=nextnode
        self.head=prevnode


    def display(self):
        print("elements are:")
        if self.head==None:
            print("empty")
        else:
             temp = self.head
             while (temp !=None):
              print(temp.data)
              temp=temp.next

obj=singlink()
n=int(input("enter how many element wants to add:"))
for i in range(n):
    p=int(input())
    obj.insertion(p)

obj.insertend(9)
obj.insertend(1)
obj.insertatsp(6,4)
obj.display()
obj.delnode(1)
obj.display()
obj.search_node(9)
obj.reverse_linst()
obj.display()

