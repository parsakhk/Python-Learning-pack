from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Binding Dropdown")
root.geometry("800x400")

def InstantKarma(event):
    if MyCombo.get() == 'Friday':
        myLabel = Label(root, text="Friday night funkin \n Yeah Yeah!").pack()
    else:
        myLabel = Label(root, text=MyCombo.get()).pack()

def selected(event):
    if clicked.get() == 'Friday':
        myLabel = Label(root, text="Friday night funkin \n Yeah Yeah!").pack()
    else:
        myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

clicked = StringVar()
clicked.set(options[2])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

MyCombo = ttk.Combobox(root, value=options)
MyCombo.current(0)
MyCombo.bind("<<ComboBoxSelected>>", InstantKarma)
MyCombo.pack()

root.mainloop()