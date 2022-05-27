from pygame import mixer
from tkinter import *
import tkinter

t=tkinter.Tk()
top = tkinter.Tk()
mixer.init()
f = Frame(top, height=600, width=500)
top.title("LOGIN GATEWAY")
f.pack()

var1 = StringVar()
var2 = StringVar()
var3 = IntVar()
global m
global m1


def playsong():
    b=var3.get()
    if b==1:
       mixer.music.load("C://Users//samya//Music//ISHARE_TERE.mpeg")
    elif b==2:
        mixer.music.load("C://Users//samya//Music//BROWN_MUNDE.mpeg")
    elif b==3:
        mixer.music.load("C://Users//samya//Music//FALLEN_FOR.mpeg")
    mixer.music.play()

    M=Message(t,test='Thanks For Using',width=100)
    M.pack()

def reset():
    var1.set("")
    var2.set("")


def checking():
    user_name = e1.get()
    password = e2.get()
    uname = '201'
    pas = 'sA@kj423'
    n = len(password)
    q = 0
    w = 0
    e = 0
    r = 0
    for i in password:
        if n >= 6 and n <= 16:
            if (i.islower()):
                q += 1
            elif (i.isupper()):
                w += 1
            elif (i.isdigit()):
                e += 1
            elif i == '@' or i == '#' or i == '$':
                r += 1
        else:
            m = Message(f, text="WRONG PASSWORD", width=100)
            m.place(x=85, y=125)
            exit()

    if q > 0 and w > 0 and e > 0 and r > 0:
        if (user_name == uname) and (password == pas):
            m1 = Message(f, text='LOGIN SUCCESSFULLY', width=100)
            m1.place(x=90, y=140)
            g = Frame(t, height=200, width=100)
            t.title("MUSIC WORLD")
            g.pack()
            c1=Checkbutton(t,text='ISHARE_TERE',variable=var3,onvalue=1,offvalue=0,height=5,width=20,
                             command=playsong)
            c2 = Checkbutton(t, text='BROWN_MUNDE', variable=var3, onvalue=2, offvalue=0, height=5, width=20,
                             command=playsong)
            c3 = Checkbutton(t, text='FALLEN_FOR', variable=var3, onvalue=3, offvalue=0, height=5, width=20,
                             command=playsong)
            c1.pack()
            c2.pack()
            c3.pack()

        else:
            m = Message(f, text="WRONG PASSWORD", width=100)
            m.place(x=85, y=125)
    else:
        m = Message(f, text="WRONG PASSWORD", width=100)
        m.place(x=85, y=125)


lb1 = Label(f, text='USERNAME', bg='blue', fg='red')
lb1.place(x=10, y=20)
lb2 = Label(f, text='PASSWORD', bg='blue', fg='red')
lb2.place(x=10, y=60)

e1 = Entry(top, textvariable=var1)
e1.place(x=200, y=20)

e2 = Entry(top, show='*', textvariable=var2)
e2.place(x=200, y=60)

b1 = Button(f, text='Login', bg='pink', command=checking)
b1.place(x=80, y=100)

b2 = Button(top, text='RESET', bg='pink', command=reset)
b2.place(x=130, y=100)
mainloop()
