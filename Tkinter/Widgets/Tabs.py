from tkinter import *
from tkinter import  ttk

root = Tk()
root.title("tabs")
root.geometry("400x400")

notebook = ttk.Notebook(root)
notebook.pack(pady=17)

my_frame1 = Frame(root, width=400, height=400, bg="blue")
my_frame2 = Frame(root, width=400, height=400, bg="red")

my_frame1.pack(fill='both', expand=1)
my_frame2.pack(fill='both', expand=1)

notebook.add(my_frame1)

root.mainloop()
