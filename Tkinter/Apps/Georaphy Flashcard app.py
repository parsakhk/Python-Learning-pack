from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Georaphy flashcard app")
root.geometry("500x500")

def states():
    Hide_all_frames()
    state_frame.pack(fill="both", expand=1)
    Our_states = ['Texas', 'Berlin', 'Sardinia', 'Tehran~1', 'Ahvaz']
    rando = randint(0, len(Our_states)-1)
    #Create states images


def capitals():
    Hide_all_frames()
    state_capitals_frame.pack(fill="both", expand=1)



#Hide all previous frames
def Hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()

my_menu = Menu(root,)
root.config(menu=my_menu)

stateMenu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Geography", menu=stateMenu)
stateMenu.add_command(label="States", command=states)
stateMenu.add_command(label="Capitals", command=capitals)
stateMenu.add_separator()
stateMenu.add_command(label="Exit", command=root.quit)
#Create frames
state_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500)



root.mainloop()