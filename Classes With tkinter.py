
from tkinter import *

root = Tk()
root.title("Classes")
root.geometry("800x400")

class Elder:
    def __init__(self, master) -> None:
        Myframe = Frame(master)
        Myframe.pack()

        self.MyButton = Button(master, text="Click me", command=self.click)

        self.MyButton.pack()

    def click(self):
        self.My_Label = Label(root, text="Hello")
        self.My_Label.pack()

Elder(root)

root.mainloop()

