
class stack:
    def __init__(self):
        self.top=-1
        self.st=list()
        self.maxs=6

    def insertion(self,x):
       if self.top==self.maxs:
           print("OVERFLOW")
       else:
           self.st.append(x)
           self.top=self.top + 1


    def delet(self):

        if self.top==-1:
            print("UNDERFLOW")
        else:
            del self.st[self.top]
            self.top -= 1


    def show(self):
        for i in self.st:
            print(i,end=' ')

obj=stack()
obj.insertion(1)
obj.insertion(3)
obj.insertion(5)
obj.insertion(7)
obj.delet()
obj.show()
