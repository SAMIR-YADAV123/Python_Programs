from tkinter import *
import tkinter
top=tkinter.Tk()

f=Frame(top,height=200,width=300)
f.pack()
e1=Entry(f,width=25,fg="green",bg="yellow")
e2=Entry(f,width=25,fg="green",bg="yellow",show='*')
e1.pack()
e2.pack()
mainloop()