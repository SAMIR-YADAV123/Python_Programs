from tkinter import*

import tkinter

top=tkinter.Tk()

top.title("frame_creation")

f=Frame(top,height=100,width=200)
Checkvar=IntVar()
#f.pack()

def display():
       x=Checkvar.get()
       if x==1:
           st="you hsve selected music"
       else:
           st="you have selected video"
       
       l=Label(f,text=st)
       l.pack()

c1=Radiobutton(top,text="Music",variable=Checkvar,value=1,height=5
               ,width=20,command=display)

c2=Radiobutton(top,text="Video",variable=Checkvar,value=2,height=5
               ,width=20,command=display)       
c1.pack()
c2.pack()
f.pack()
#w.pack()
mainloop()
