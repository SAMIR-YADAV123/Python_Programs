from tkinter import*
root=Tk()
def buttonclick():
       print("samir yadav")
f=Frame(root,height=600,width=500)
b=Button(f,text="click",width=15,height=3,bg="red",fg='orange',command=buttonclick)
b.pack()
f.pack()       
mainloop()
