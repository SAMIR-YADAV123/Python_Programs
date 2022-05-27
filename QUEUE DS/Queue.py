class queue:
    def __init__(self):
      self.qu=list()
      self.max=6
      self.f=-1
      self.r=-1

    def insert(self,x):
        if self.r==self.max:
           print("OVERFLOW")

        elif self.r == -1:
            self.f += 1
            self.r += 1
            self.qu.append(x)
        else:
            self.r+=1
            self.qu.append(x)

    def delt(self):
        if self.f==-1 and self.r==-1:
            print("UNDERFLOW")
        elif self.f==self.r:
            self.qu.pop()
            self.f=self.r=-1
        else:
           del self.qu[self.f]


    def show(self):
        for i in self.qu:
           print(i,end=" ")
           self.f+=1
        print("\narray",self.qu)



obj=queue()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.delt()
obj.delt()
obj.show()






