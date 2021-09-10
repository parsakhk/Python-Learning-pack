from tkinter import *
from PIL import Image, ImageTk

def Func2():
    Butoon4 = Button(frameTest, text="Hehe :)", command=Func1)
    Butoon4.grid(row=1, column=2)
    Butoon5 = Button(frameTest, text="Hehe :0", command=Func1)
    Butoon5.grid(row=6, column=2)

def Func1():
    Butoon2 = Button(frameTest, text="Hehe :)", command=Func2)
    Butoon2.grid(row=7, column=6)
    Butoon3 = Button(frameTest, text="Hehe :0", command=Func2)
    Butoon3.grid(row=4, column=5)

def Func():
    Butoon1 = Button(frameTest, text="Hehe", command=Func1)
    Butoon1.grid(row=3, column=7)

def Secret():
    label = Label(frameTest, text="Hello little shit")
    label.grid(row=3, column=2)
    Butoon = Button(frameTest, text="Hehe i duplicated myself", command=Func)
    Butoon.grid(row=8, column=6)

root = Tk()
root.title("Frames")

frameTest = LabelFrame(root, text="This my shit label frame", pady=50, padx=50)
frameTest.pack(padx=10, pady=10)

b = Button(frameTest, text="I am in frame little....", command=Secret)
b2 = Button(frameTest, text="I am the another button ;)")
b.grid(row=0, column=2)
b2.grid(row=2, column=2)

root.mainloop()