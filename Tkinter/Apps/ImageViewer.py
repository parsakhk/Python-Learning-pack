from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("ImageViewer")
#Imorting Images
myimg = ImageTk.PhotoImage(Image.open("./Assets/ImageViewer/terrarian.png"))
myimg2 = ImageTk.PhotoImage(Image.open("./Assets/ImageViewer/IMG-20200923-WA0002.jpg.png"))
myimg4 = ImageTk.PhotoImage(Image.open("./Assets/ImageViewer/Amethyst.png"))

Img_list = [myimg, myimg2,myimg4]

my_label = Label(image=myimg)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text="Image 1/" + str(len(Img_list)), bd=1, relief=SOLID, anchor=E)


def forward(Image_num):
    global my_label
    global button_after
    global button_back

    my_label.grid_forget()
    my_label = Label(image=Img_list[Image_num + 1])
    button_after = Button(root, text=">>", command=lambda: forward(Image_num+1))
    button_back = Button(root, text="<<", command=lambda: backward(Image_num-1))

    if Image_num == 3:
        button_after = Button(root, text=">>", state=DISABLED)
        button_after.grid(row=1, column=1)

    my_label.grid(row=0, column=0, columnspan=3)


    button_back.grid(row=1, column=0)
    button_after.grid(row=1, column=1)
    button_quit.grid(row=1, column=2)

    status = Label(root, text="Image " + str(Image_num) + "/" + str(len(Img_list)), bd=1, relief=SOLID, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def backward(Image_num):
    global my_label
    global button_after
    global button_back

    my_label.grid_forget()
    my_label = Label(image=Img_list[Image_num - 1])
    button_after = Button(root, text=">>", command=lambda: forward(Image_num+1))
    button_back = Button(root, text="<<", command=lambda: backward(Image_num-1))

    if Image_num == 3:
        button_after = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_after.grid(row=1, column=1)
    #Update status bar
    status = Label(root, text="Image " + str(Image_num) + "/" + str(len(Img_list)), bd=1, relief=SOLID, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=backward, state=DISABLED)
button_after = Button(root, text=">>",command=lambda: forward(1))
button_quit = Button(root, text="Quit", command=root.quit)

button_back.grid(row=1, column=0)
button_after.grid(row=1, column=1)
button_quit.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
