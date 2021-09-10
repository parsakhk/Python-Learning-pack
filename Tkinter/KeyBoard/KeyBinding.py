from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("KeyBinding")
root.geometry("400x400")

def clicker(event):
    e = Entry(root, width=30)
    e.pack()

myButton = Button(root, text="Click me")
myButton.bind("<Button-3>", clicker)
myButton.pack(pady=20)




root.mainloop()

