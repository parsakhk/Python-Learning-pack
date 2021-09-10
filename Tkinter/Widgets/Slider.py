from tkinter import *

root = Tk()
root.title("Slider")
root.geometry("400x400")

def Click():
    my_label = Label(root, text=vertical.get()).pack()
    root.geometry(str(vertical.get()) + "x400")

vertical = Scale(root, from_=0, to=1000)
vertical.pack()

button = Button(root, text="Click me!", command=Click)
button.pack()

root.mainloop()