from tkinter import*
parent = Tk()
parent.title("FIRST FORM OF GUI")
parent.geometry("700x600")

regf = Label(parent,text = "REGISTRATION FORM")
regf.place(x=200,y=40)

name=Label(parent,text="Name: ")
name.place(x=60,y=100)
e1=Entry(parent)
e1.place(x=160,y=100)

fname=Label(parent,text="Father's Name: ")
fname.place(x=60,y=140)
e2=Entry(parent)
e2.place(x=160,y=140)

mname=Label(parent,text="Mother's Name: ")
mname.place(x=60,y=180)
e3=Entry(parent)
e3.place(x=160,y=180)

mob=Label(parent,text="Mobile No.: ")
mob.place(x=60,y=220)
e4=Entry(parent)
e4.place(x=160,y=220)

res=Label(parent,text="Residence: ")
res.place(x=60,y=260)
e5=Entry(parent)
e5.place(x=160,y=260)

gender=Label(parent,text="GENDER:")
gender.place(x=60,y=300)

cb1=Checkbutton(parent, text="Male")
cb1.place(x=160,y=300)

cb2=Checkbutton(parent, text="Female")
cb2.place(x=250,y=300)

lq=Label(parent,text="Last Qualification:")
lq.place(x=60,y=340)

cb3=Checkbutton(parent, text="10th Pass")
cb3.place(x=160,y=360)

cb4=Checkbutton(parent, text="12th Pass")
cb4.place(x=160,y=390)

cb5=Checkbutton(parent, text="Graduate")
cb5.place(x=160,y=420)

sub=Label(parent,text="You can submit the form only once")
sub.place(x=80,y=460)
sbtn1=Button(parent,text="SUBMIT")
sbtn1.place(x=160,y=480)

parent.mainloop()
