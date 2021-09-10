from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("RadioButtons")

# r = IntVar()
# r.set("2")

MODES = [
    ("Pepperoni", "1st"),
    ("Cheese", "2nd"),
    ("Mushroom", "3rd"),
    ("PineApple", "4rth")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode, in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    mylabel = Label(root, text=pizza.get())
    mylabel.pack()

# Radiobutton(root, text="Tea", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Cookie", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# mylabel = Label(root, text=pizza.get())
# mylabel.pack()

myButton = Button(root, text="Clicked me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()