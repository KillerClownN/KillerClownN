from tkinter import *
top=Tk()
top.geometry("700x500")
x=Canvas(top,height=400,width=400,bg="#0DC9EF")
x.pack()
x.create_oval(130,50,280,200,outline="black",fill="white",width=4)
x.create_oval(110,200,300,400,outline="black",fill="white",width=4)
x.create_oval(165,80,195,110,outline="black",fill="black")
x.create_oval(220,80,250,110,outline="black",fill="black")
x.create_line(175,150,205,170,240,150,smooth="true",width=4)
x.create_line(165,150,205,200,245,150,smooth="true",width=4, fill="black")

top.mainloop()
