from tkinter import *
from tkinter import messagebox

def popup():
    while True:
        messagebox.showinfo("Your computer feels hell!", "Your computer feels hell!")

root = Tk()
root.title("MessageBoxes")

Button(root, text="Hello", command=popup).pack()

root.mainloop()