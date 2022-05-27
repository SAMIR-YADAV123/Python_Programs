import tkinter as tk
top=tk.Tk()

w=tk.Label(top,text="RED SUN",bg='red',fg='white')
w.pack(fill=tk.X,pady=20)
w=tk.Label(top,text="Green Grass",bg='Green',fg='Black')
w.pack(fill=tk.X,pady=10)
w=tk.Label(top,text="Blue sky",bg='blue',fg='white')
w.pack(fill=tk.X,pady=10)


w=tk.Label(top,text="RED SUN",bg='red',fg='white')
w.pack(padx=5,pady=10,side=tk.LEFT)
w=tk.Label(top,text="Green Grass",bg='Green',fg='Black')
w.pack(padx=5,pady=10,side=tk.LEFT)
w=tk.Label(top,text="Blue sky",bg='blue',fg='white')
w.pack(padx=5,pady=10,side=tk.LEFT)

w=tk.Label(top,text="RED SUN",bg='red',fg='white')
w.pack()
w=tk.Label(top,text="Green Grass",bg='Green',fg='Black')
w.pack(fill=tk.X,ipadx=10)
w=tk.Label(top,text="Blue sky",bg='blue',fg='white')
w.pack(fill=tk.X,ipady=10)

w=tk.Label(top,text="RED SUN",bg='red',fg='white')
w.place(x=20,y=30,width=100,height=50)
w=tk.Label(top,text="Green Grass",bg='Green',fg='Black')
w.place(x=20,y=100,width=100,height=50)
w=tk.Label(top,text="Blue sky",bg='blue',fg='white')
w.place(x=200,y=100,width=100,height=50)
tk.mainloop()