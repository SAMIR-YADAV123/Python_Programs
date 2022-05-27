from tkinter import*

import tkinter
top=tkinter.Tk()

f=Frame(top,height=200,width=300)
f.pack()

var1=IntVar()
var2=StringVar()

def display():
      x=var1.get()
      y=var2.get()
      
      l1=Message(f,text=x,width=100)
      l1.pack()
      if y=='mango':
         l2=Message(f,text=y,width=100)
         l2.pack()
      
s1=Spinbox(f,from_=5,to=15,textvariable=var1,width=15,fg='blue')
s2=Spinbox(f,values=('apple','banana','mango'),textvariable=var2,width=15,fg='blue')
b=Button(f,text='click',command=display) 
s1.pack()
s2.pack()
b.pack()
mainloop()     