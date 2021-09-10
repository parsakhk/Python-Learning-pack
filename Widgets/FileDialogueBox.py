from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("FileDialogue")

def Open():
    global my_image
    global my_imageLbl
    global mylabel
    root.filename = filedialog.askopenfilename(initialdir="./Assets", title="Select file", filetypes=(("Png files", "*.png"), ("JPG files", "*.jpg")))
    mylabel = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_imageLbl = Label(root, image=my_image).pack()

my_btn = Button(root, text="Open file", command=Open).pack()

root.mainloop()