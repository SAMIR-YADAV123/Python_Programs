from tkinter import*
import tkinter
top=tkinter.Tk()
f=Frame(top,height=200,width=300)
f.pack()

lb=Listbox(f,height=20,width=10,selectmode=SINGLE)
lb.insert(0,'mango')
lb.insert(1,'apple')
lb.insert(2,'papaya')
lb.insert(3,'guava')

def on_select(event):
     st=""
     ind=lb.curselection()
     for i in ind:
         st+=lb.get(i)
     te=Label(f,text=st,width=100)
     te.pack()
     
lb.bind("<<ListboxSelect>>",on_select)
lb.pack()
mainloop()     