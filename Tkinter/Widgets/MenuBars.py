from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Menu")
root.geometry("400x400")


my_menu = Menu(root)
root.config(menu=my_menu)

#ساخت دستور برای ایتم های منو
def Exit():
    root.quit()

def Open():
    filedialog.askopenfile()

def Save():
    filedialog.asksaveasfile()
def clear():
    e.delete(0, END)
def copy():
    pass
def Info():
    messagebox.showinfo("اطلاعات", "This program made to teach you about Menus")
#ساخت ایتم منو

e = Entry(root, width=30)
e.pack()

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File ", menu=file_menu)
file_menu.add_command(label="Open", command=Open)
file_menu.add_command(label="Save", command=Save)
# برای جدا کردن ایتم ها
file_menu.add_separator()
file_menu.add_command(label="Exit", command=Exit)

# بریم یک منوی دیگر بسازیم
edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=copy)
# یک منو درباره اطلاعات برنامه بسازیم
Inform_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Support", menu=Inform_menu)
Inform_menu.add_command(label="Info", command=Info)

root.mainloop()
