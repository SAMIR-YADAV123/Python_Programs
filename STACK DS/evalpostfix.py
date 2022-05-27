class evale:
    def __init__(self,cap):
        self.top=-1
        self.cap=cap
        self.arr=[]

    def evaluate(self,aa):
        for i in aa:
            if i.isdigit():
                self.arr.append(i)
                self.top=self.top+1
            else:
                n=len(self.arr)
                x=self.arr.pop(n-1)
                y=self.arr.pop(n-2)
                self.top-=2
                self.arr.append(str(eval(x + i + y)))

    def display(self):
        print("evaluate result is:",self.arr[0])

exp= "17463**+-"
obj=evale(len(exp))

obj.evaluate(exp)
obj.display()
