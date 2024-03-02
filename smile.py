from tkinter import *
top=Tk()
top.geometry("700x500")
x=Canvas(top,height=400,width=400,bg="#E6E6FA")
x.pack()
x.create_oval(50,50,300,300,outline="black",fill="yellow")
x.create_oval(120,100,150,150,outline="black",fill="white")
x.create_oval(190,100,220,150,outline="black",fill="white")
x.create_oval(120,115,150,150,outline="black",fill="black")
x.create_oval(190,115,220,150,outline="black",fill="black")
x.create_line(120,200,170,250,220,200,smooth="true",width=4, fill="black")

top.mainloop()
