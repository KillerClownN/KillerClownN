from tkinter import *   

top = Tk()       
c = Canvas(top,bg = "pink",height = "500", width="500")
roof=c.create_line(50, 100, 100, 50, width=5)
roof=c.create_line(100, 49, 150, 100, width=5)
roof=c.create_line(98,51,300,49,width=5)

outline=c.create_line(300,49,300,299,width=5)
outline=c.create_line(300,299,50,300,width=5)
outline=c.create_line(50,300,51,99,width=5)
outline=c.create_line(51,99,300,99,width=5)
outline=c.create_line(98,51,300,49,width=5)
outline=c.create_line(150,100,149,300,width=5)
circle=c.create_oval(200,150,250,200,outline = "black",fill = "white",width = 2)



c.pack()
  
top.mainloop()  

