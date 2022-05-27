#Impporting tkinter module
from tkinter import*

#In order to create a tkinter application, we generally create an instance of tkinter frame, i.e., Tk().
# It helps to display the root window and manages all the other components of the tkinter application

top=Tk()
top.title("CALCULATOR")

#Global variable

num1=0
ind=0

def enter(n):
    cu=e.get()
    e.delete(0,END)
    e.insert(0,str(cu)+str(n))
    
def add():
    global num1
    num1=float(e.get())
    global ind
    ind=1
    e.delete(0,END)

def sub():
    global num1
    num1=float(e.get())
    global ind
    ind = 2
    e.delete(0, END)

def mul():
    global num1
    num1 = float(e.get())
    global ind
    ind = 3
    e.delete(0, END)

def div():
    global num1
    num1=float(e.get())
    global ind
    ind = 4
    e.delete(0, END)
    
def modul():
    global num1
    num1=float(e.get())
    global ind
    ind=5
    e.delete(0,END)

def clear():
  e.delete(0,END)

def back():
    cur=int(e.get())
    cur=cur//10
    e.delete(0,END)
    e.insert(0,cur)

def equal():
   num2=float(e.get())
   e.delete(0,END)
   if ind==1:
       e.insert(0,float(num1+num2))
   elif ind==2:
       e.insert(0,float(num1-num2))
   elif ind==3:
       e.insert(0,float(num1*num2))
   elif ind==4:
        e.insert(0,float(num1/num2))
   elif ind==5:
        e.insert(0,int(num1 % num2))

e=Entry(top,width=50,borderwidth=6)
e.grid(row=0,column=0,columnspan=3)

b1=Button(top,text='1',command=lambda:enter(1),padx=50,pady=20).grid(row=1,column=0)
b2=Button(top,text='2',command=lambda:enter(2),padx=50,pady=20).grid(row=1,column=1)
b3=Button(top,text='3',command=lambda:enter(3),padx=50,pady=20).grid(row=1,column=2)
b4=Button(top,text='4',command=lambda:enter(4),padx=50,pady=20).grid(row=1,column=3)
b5=Button(top,text='5',command=lambda:enter(5),padx=50,pady=20).grid(row=2,column=0)
b6=Button(top,text='6',command=lambda:enter(6),padx=50,pady=20).grid(row=2,column=1)
b7=Button(top,text='7',command=lambda:enter(7),padx=50,pady=20).grid(row=2,column=2)
b8=Button(top,text='8',command=lambda:enter(8),padx=50,pady=20).grid(row=2,column=3)
b9=Button(top,text='9',command=lambda:enter(9),padx=50,pady=20).grid(row=3,column=0)
b10=Button(top,text='0',command=lambda:enter(0),padx=50,pady=20).grid(row=3,column=1)
b11=Button(top,text='.',command=lambda:enter('.'),padx=50,pady=20).grid(row=4,column=2)
b12=Button(top,text='%',command=modul,padx=50,pady=20).grid(row=4,column=3)
b13=Button(top,text='+',command=add,padx=50,pady=20).grid(row=3,column=2)
b14=Button(top,text='-',command=sub,padx=50,pady=20).grid(row=3,column=3)
b15=Button(top,text='*',command=mul,padx=50,pady=20).grid(row=4,column=0)
b16=Button(top,text='/',command=div,padx=50,pady=20).grid(row=4,column=1)
b17=Button(top,text='clear',command=clear,padx=50,pady=20).grid(row=5,column=3)
b18=Button(top,text='=',command=equal,padx=50,pady=20).grid(row=5,column=0,columnspan=2)
b19=Button(top,text='BACK',command=back,padx=50,pady=20).grid(row=5,column=2)

# It tells Python to run the Tkinter event loop
top.mainloop()