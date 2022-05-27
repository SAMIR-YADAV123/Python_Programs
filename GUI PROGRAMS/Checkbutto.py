from tkinter import*
import tkinter

root=tkinter.Tk()
f=Frame(root,height=500,width=400)
f.pack()

var=IntVar()

def display():
    x=var.get()
    
    if x==1:
        m=Message(f,text='you have selected Reading',width=100)
        m.pack()
    else:
        m=Message(f,text='you have selected singing',width=100)
        m.pack()
        
cb1=Checkbutton(root,text='Reading',variable=var,onvalue=1,offvalue=0,height=6,width=20,command=display)       
cb1.pack()

cb2=Checkbutton(root,text='Singing',variable=var,onvalue=2,offvalue=0,height=6,width=20,command=display)       
cb2.pack()
mainloop()