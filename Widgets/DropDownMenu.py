from tkinter import *
from PIL import Image, ImageTk

def show():
    mylabel = Label(root, text=clicked.get())
    mylabel.pack()

root = Tk()
root.title("DropdownMenu")
root.geometry("400x400")

Options = [
    "Parsa",
    "Behzad",
    "Hamide",
    "Marefat",
    "Radin",
    "Soraya",
]

clicked = StringVar()
clicked.set(Options[0])

drop = OptionMenu(root, clicked, *Options)
drop.pack(pady=20, padx=30)

Mybutton = Button(root, text="Shows Collection", command=show, padx=10, pady=20)
Mybutton.pack()

root.mainloop()