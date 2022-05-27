from tkinter import*
master=Tk()

w=Canvas(master,width=500,height=600)
w.create_line(10,10,100,10,150,10,150,150,width=2,fill="red")

w.create_oval(50,100,150,200,width=2,fill="yellow",outline="green",activefill="orange")

fnt=("times",30,"bold italic")
w.create_text(400,50,text="samir yadav",font=fnt,fill="orange",activefill="black")

point=[150,100,200,120,240,180,210,200,150,150,100,200]
w.create_polygon(point,fill="black",activefill="red")

w.create_rectangle(200,300,500,600,fill='black',activefill='pink')

w.create_arc(100,100,400,300,width=3,start=270,extent=180,outline="red",style=
             'arc')
w.pack()


mainloop()