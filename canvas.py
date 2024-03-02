from tkinter import *   

top = Tk()    
top.geometry("400x500")   
c = Canvas(top,bg = "pink",height = "200", width="400")
arc = c.create_arc(250,10,350,400,start = 0,extent = 180, fill= "white")
rect=c.create_rectangle(20,5,110,110,outline ="black",fill ="white",width = 5)
circle=c.create_oval(150,20,250,150,outline = "black",fill = "white",width = 2)
line=c.create_line(150,20,250,150,fill="blue")
line=c.create_line(50,150,250,20,fill="blue")

c.pack()
  
top.mainloop()  
