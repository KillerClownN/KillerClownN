#Object- write a python gui program to make a simple calculator using tkinter module
from tkinter import*

top=Tk()
top.geometry("700x500")
mytext=StringVar()

label_1=Label(top,text=("Enter number 1:"))
label_1.grid(row=1, column=1)
e1=Entry(top,bg='lightpink')
e1.grid(row=1,column=2)

label_2=Label(top,text=("Enter number 2:"))
label_2.grid(row=2, column=1)
e2=Entry(top,bg='lightpink')
e2.grid(row=2,column=2)

def add():
    e3=int(e1.get())+int(e2.get())
    mytext.set(e3)

def sub():
    e4=int(e1.get())-int(e2.get())
    mytext.set(e4)

def multiply():
    e5=int(e1.get())*int(e2.get())
    mytext.set(e5)

def divide():
    e6=int(e1.get())/int(e2.get())
    mytext.set(e6)
    
def power():
    e7=int(e1.get())**int(e2.get())
    mytext.set(e7)


btn1=Button(top,text="ADD",command=add)
btn1.place(x=20,y=80)

btn2=Button(top,text="SUB",command=sub)
btn2.place(x=20,y=110)

btn3=Button(top,text="MULTIPLY",command=multiply)
btn3.place(x=20,y=140)

btn4=Button(top,text="DIVIDE",command=divide)
btn4.place(x=20,y=170)

btn5=Button(top,text="POWER",command=divide)
btn5.place(x=20,y=200)

result=Label(top,textvariable=mytext)
result.place(x=80,y=230)

top.mainloop()
    
