class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class dlinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def addatstart(self,x):
       newnode=Node(x)
       newnode.next=None 
       if self.head==None:
             self.head=self.tail=newnode
             newnode.previous=None
             newnode.next=None
            
       else:
                   
            self.head.previous=newnode
            newnode.next=self.head
            newnode.previous=None
            self.head=newnode
            self.head.previous=None
          
       


    def addatend(self,x):
        newnode=Node(x)
       
        if self.head==None:
           self.head=self.tail=newnode
           self.head.next=None
           self.tail.previous=None
          
        else :
           self.tail.previous=newnode
           newnode.previous=self.tail
           self.tail=newnode
           self.tail.next=None
               
    

    def addatsp(self,x,y):
   
       newnode=Node(x)
       temp=self.head 
       i=1
       while(i<y-1):
          temp=temp.next
          i+=1
          
       newnode.previous=temp
       newnode.next=temp.next
       temp.next.previous=newnode
       temp.next=newnode
  
  
    def removestart(self):
        
        if(self.head==None):
              print("Empty list")
        else:
            if self.head==self.tail:
                self.head=self.tail=None
            else:
               self.head=self.head.next
               self.head.previous=None
               
    def removend(self):
      if(self.tail==None):
         print("list is empty")
      else:
            if(self.head==self.tail):
              self.tail=self.head=None
            else:
                self.tail=self.tail.next
                self.tail.next = None              
        
               
    def removespe(self, x):
        temp=self.head
        while temp!=None:
          if temp.data==x:
               if self.head==temp:
                  self.head=self.head.next
                  self.head.previous=None
                  temp=None  
               elif self.tail==temp:
                   self.tail=self.tail.previous
                   self.tail.next=None
                   temp=None
               else:
                    temp.previous.next=temp.next
                    temp.next.previous=temp.previous
                    temp=None
          else:
              temp=temp.next      


    def display(self):
        current = self.tail
        while(current !=None):
            print(current.data,end=" ")
            current=current.next

dList = dlinked()
dList.addatstart(1)
dList.addatstart(2)
dList.addatstart(4)
dList.addatstart(5)
dList.display()
dList.addatend(6)
dList.display()
dList.addatsp(3,3)
dList.display()
dList.removend()
dList.removestart()
dList.removespe(2)
dList.display()