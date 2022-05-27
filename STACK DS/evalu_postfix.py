class Evaluate:
 def __init__(self, capacity):
    self.top = -1
    self.capacity = capacity
    self.array = []
 def isEmpty(self):
   if self.top == -1:
     return True
   else:
     return False
 def peek(self):
     return self.array[-1]
 def pop(self):
   if not self.isEmpty():
     self.top -= 1
     return self.array.pop()
   else:
     return "$"
 def push(self, op):
    self.top += 1
    self.array.append(op)
 def evaluatePostfix(self, exp):
    for i in exp:
     if i.isdigit():
       self.push(i)
     else:
       val1 = self.pop()
       val2 = self.pop()
       self.push(str(eval(val2 + i + val1)))
       return int(self.pop())
# Program to test above function
exp = "234+*5*"
print ("\nPostfix Notation : ",exp)
obj = Evaluate(len(exp))
print ("Postfix Evaluation : ",obj.evaluatePostfix(exp))