from tkinter import*
import tkinter
top=tkinter.Tk()


f=Frame(top,height=600,width=500)
top.title("LOGIN GATEWAY")
f.pack()
 
var1=StringVar()
var2=StringVar()

global m
global m1

def reset():
    var1.set("")
    var2.set("")
    
def checking():
    user_name = e1.get()
    password = e2.get()
   
    uname='20Q12345'
    pas='Sist@13245768'
    n=len(password)
    q=0
    w=0
    e=0
    r=0
    for i in password:
         if n>=6 and n<=16:
              if (i.islower()):
                q+=1
              elif (i.isupper()):
                 w+=1
              elif(i.isdigit()):
                 e+=1
              elif i=='@' or i=='#' or i=='$':
                 r+=1
         else:
             m=Message(f,text="WRONG PASSWORD",width=100)
             m.place(x=85,y=125)
             exit()
         
    if q>0 and w>0 and e>0 and r>0:
            if (user_name==uname) and (password==pas):
                m1=Message(f,text='LOGIN SUCCESSFULLY',width=100)
                m1.place(x=90,y=140)
            else:    
                 m=Message(f,text="WRONG PASSWORD",width=100)
                 m.place(x=85,y=125)
    else:
             m=Message(f,text="WRONG PASSWORD",width=100)
             m.place(x=85,y=125)

lb1=Label(f,text='USERNAME',bg='blue',fg='red')
lb1.place(x=10,y=20)
lb2=Label(f,text='PASSWORD',bg='blue',fg='red')
lb2.place(x=10,y=60)

e1=Entry(top,textvariable=var1)
e1.place(x=200,y=20)

e2=Entry(top,show='*',textvariable=var2)
e2.place(x=200,y=60)

b1=Button(f,text='Login',bg='pink',command=checking)
b1.place(x=80,y=100)

b2=Button(top,text='RESET',bg='pink',command=reset)
b2.place(x=130,y=100)
mainloop()