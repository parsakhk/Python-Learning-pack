from tkinter import *


root = Tk()
root.title("round buttons")

def thing():
    img_label.config(text='you clicked')

img = PhotoImage(file="./Tkinter/Apps/Assets/ImageViewer/terrarian.png")

mylabel = Label(image=img)


mybutton = Button(root, image=img, command=thing, borderwidth=10)
mybutton.pack(pady=25)

img_label = Label(root, text='')
img_label.pack()

root.mainloop()
