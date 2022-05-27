class convert:
    precedence={'^':5,"*":4,"/":3,"+":3,"-":3,'(':2,")":1}
    def __init__(self):
         self.item=[]
         self.size=-1

    def push(self,value):
          self.item.append(value)
          self.size+=1

    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size-=1
            return  self.item.pop()

    def isempty(self):
         if self.size==-1:
             return  True
         else:
              return False
    def seek(self):
        if self.isempty():
            return True
        else:
            return self.item[self.size]

    def isoperand(self,i):
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return  True
        else:
            return False

    def infixtopost(self,expr):
        postfix=""
        for i in expr:
            if(len(expr)%2==0):
                return False
            elif self.isoperand(i):
                 postfix+=i
            elif (i in '+-*/^'):
                while(len(self.item) and self.precedence[i]<=self.precedence[self.seek()]):
                     postfix+=self.pop()
                self.push(i)
            elif i == '(':
               self.push(i)
            elif i == ')':
              o=self.pop()
              while o!="(":
                   postfix+=o
                   o=self.pop()

        while len(self.item):
             if(self.seek()=="("):
                 self.pop()
             else:
                 postfix+=self.pop()
        return  postfix

s=convert()
expr=('A+(B*C-(D/E-F)*G)*H')
print("INFIX NOTATION:",expr)
result=s.infixtopost(expr)
if result!=False:
    print("POSTFIX NOTATION:",result)

