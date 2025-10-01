import tkinter
from tkinter import *
windows =Tk()
windows.title("My Calculator")
windows.geometry('550x370')
windows.config(background='black')
e = Entry(windows , width=74,border=5,bg='white',foreground="black")
e.place(x=0,y=0)

def click(num):
    r= e.get()
    e.delete(0,END)
    e.insert(0, str(r)+str(num))


b=Button(windows ,text="1",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue" ,command = lambda:click(1))
b.place(x=10,y=90)


b=Button(windows ,text="2",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(2))
b.place(x=140,y=90)

b=Button(windows ,text="3",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(3))
b.place(x=270,y=90)


b=Button(windows ,text="4",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(4))
b.place(x=10,y=140)


b=Button(windows ,text="5",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(5))
b.place(x=140,y=140)


b=Button(windows ,text="6",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(6))
b.place(x=270,y=140)


b=Button(windows ,text="7",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(7))
b.place(x=10,y=190)


b=Button(windows ,text="8",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(8))
b.place(x=140,y=190)


b=Button(windows ,text="9",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(9))
b.place(x=270,y=190)


b=Button(windows ,text="0",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click(0))
b.place(x=140,y=240)


b=Button(windows ,text=".",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command = lambda:click('.'))
b.place(x=270,y=240)

def clr():
    e.delete(0,END)

b=Button(windows ,text="clear",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue" ,command=clr)
b.place(x=10,y=240)

def add():
     n1=e.get()
     global t
     global fun
     fun='add'
     t= float(n1)
     e.delete(0,END)

b=Button(windows ,text="+",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command=add)
b.place(x=400,y=90)


def sub():
    n1 = e.get()
    global t
    global fun
    fun = "sub"
    t = float(n1)
    e.delete(0, END)

b=Button(windows ,text="-",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command=sub)
b.place(x=400,y=140)


def mul():
    n1 = e.get()
    global t
    global fun
    fun = "mul"
    t = float(n1)
    e.delete(0, END)

b=Button(windows ,text="*",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command=mul)
b.place(x=400,y=190)


def div():
    n1 = e.get()
    global t
    global fun
    fun = "div"
    t = float(n1)
    e.delete(0, END)
b=Button(windows ,text="/",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command=div)
b.place(x=400,y=240)


def mod():
    n1 = e.get()
    global t
    global fun
    fun = "mod"
    t = float(n1)
    e.delete(0, END)

b=Button(windows ,text="%",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command=mod)
b.place(x=140,y=290)


def sqr():
    n1 = e.get()
    global t
    t = float(n1)
    e.delete(0, END)
    e.insert(0, t ** 2)

b=Button(windows ,text="**",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command=sqr)
b.place(x=270,y=290)


def half():
    n1 = e.get()
    global t
    t = float(n1)
    e.delete(0, END)
    e.insert(0, t / 2)

b=Button(windows ,text="1/2",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command=half)
b.place(x=10,y=290)
def end():
    n2=e.get()
    e.delete(0,END)
    if fun=="add":
       e.insert(0, t+float(n2))
    elif fun=="sub":
        e.insert(0,t-float(n2))
    elif fun=="mul":
        e.insert(0,t*float(n2))
    elif fun=="div":
        e.insert(0,t/float(n2))
    elif fun=="mod":
        e.insert(0,t%float(n2))





b=Button(windows ,text="=",width=10,height=2,foreground='red',activebackground="red",activeforeground="blue",command=end)
b.place(x=400,y=290)
mainloop()