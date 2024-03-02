#Object- write a python gui program to calculate the area and perimeter of circle using tkinter module
from tkinter import*

top=Tk()
top.geometry("700x500")
mytext=StringVar()

label_1=Label(top,text=("Enter radius of circle:"))
label_1.grid(row=1, column=1)
e1=Entry(top,bg='lightpink')
e1.grid(row=1,column=2)


def area():
    e3=int(e1.get())**2*22/7
    mytext.set(e3)

def perimeter():
    e4=int(e1.get())*2*22/7
    mytext.set(e4)
    
btn1=Button(top,text="area",command=area)
btn1.place(x=20,y=80)

btn2=Button(top,text="perimeter",command=perimeter)
btn2.place(x=80,y=80)

result=Label(top,textvariable=mytext)
result.place(x=80,y=120)

top.mainloop()
    
