from tkinter import *

root = Tk()
root.title("Pack&Grid Forget")
root.geometry("800x400")

My_Label = Label(root)

# def Delete():
#     My_Label.pack_forget()
#     Suhmoiujt['state'] = NORMAL


def Suujsjhsj():
    global My_Label
    My_Label.destroy()
    My_Label = Label(root, text="سلام " + e.get(), font=("IranSans", 43))
    e.delete(0, END)
    My_Label.pack(padx=10, pady=10)
    Suhmoiujt['state'] = DISABLED

e = Entry(root, width=50, font=("IranSans", 30))
e.pack()

Suhmoiujt = Button(root, text="Submit", command=Suujsjhsj)
Suhmoiujt.pack(padx=10, pady=10)

# delelete = Button(root, text="Delete", command=Delete)
# delelete.pack(padx=10, pady=10)

root.mainloop()
