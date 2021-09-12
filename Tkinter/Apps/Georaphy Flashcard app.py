from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Georaphy flashcard app")
root.geometry("500x600")

def state_answer():
    answer = answer_input.get()
    answer.replace(" ", "")

    if answer == Our_states[rando]:
        Correct = "Correct! " + Our_states[rando]
    else:
        Correct = "Try again! " + Our_states[rando]

    answer_label.config(text=Correct)

def states():
    Hide_all_frames()
    state_frame.pack(fill="both", expand=1)
    global Our_states
    Our_states = ['Texas', 'Berlin', 'Sardinia', 'Tehran', 'Ahvaz']
    global rando
    rando = randint(0, len(Our_states)-1)
    rando_state = "./Tkinter/Apps/Assets/Geography Flashcard App/" + Our_states[rando] + ".png"

    #Create states images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(rando_state))
    show_state = Label(state_frame, image=state_image)
    show_state.pack(pady=7)
    global answer_input
    answer_input = Entry(state_frame, font=("Helvetica", 18))
    answer_input.pack(pady=15)
    #Rando Button
    rando_Button = Button(state_frame, text="Next state", command=states)
    rando_Button.pack(pady=10)
    answer_button = Button(state_frame, text="Answer", command=state_answer)
    answer_button.pack(pady=5)
    global answer_label
    answer_label = Label(root, text='')
    answer_label.pack(pady=5)

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