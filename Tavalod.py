from tkinter import *


from PIL import ImageTk, Image

root = Tk()
root.title("تولدت مبارک!")
root.geometry("400x600")


def Submit():
    label = Label(root, text="تولدت مبارک " + Tavalod_entry.get(), font=("IranSans", 35))
    label.grid(row=2, column=0, columnspan=2)

Tavalod_entry = Entry(root, width=39, border=2, relief=SOLID)
Tavalod_entry.grid(row=0, column=1)

Tavold_label = Label(root, text="Enter your name", bd=2, relief=SOLID)
Tavold_label.grid(row=0, column=0, padx=20)

SubmitButton = Button(root, text="Submit", bg="light gray", bd=2, relief=SOLID, command=Submit)
SubmitButton.grid(row=1, column=0, columnspan=2, pady=10, padx=20, ipadx=135)

root.mainloop()