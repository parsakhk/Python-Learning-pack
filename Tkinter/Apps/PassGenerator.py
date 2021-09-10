from tkinter import *
from random import randint
from tkinter import messagebox

root = Tk()
root.title("Password generator")
root.geometry("420x420")
root.iconbitmap("D:\Parsa\PRoject\Tkinter\Apps\Assets\Icon.ico")


def new_rand():
    # Clear out our Pw entry
    pw_Entry.delete(0, END)

    #Get pass length
    pw_length = int(myEntry.get())

    # create varibale for whole pass
    my_password = ''

    #Loop through pass length 
    for x in range(pw_length):
        my_password += chr(randint(33,136)) 

    # Output pass on the screen
    pw_Entry.insert(0, my_password)      


def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_Entry.get())
    messagebox.showinfo("Info", "Your Password is in clipboard now!")

#Make Label frame
If = LabelFrame(root, text="How many Characters you want?")
If.pack(pady=20)
#Make char entry
myEntry = Entry(If, font=("Arial", 20))
myEntry.pack(pady=20, padx=20)
#Make password entry
pw_Entry = Entry(root, text='', font=("Arial", 24), bd=0, bg="systembuttonface")
pw_Entry.pack(pady=30)
#Create button frame
my_Frame = Frame(root)
my_Frame.pack(pady=20)
#Create gen button
myButton = Button(my_Frame, text="Generate Powerfull Password", command=new_rand)
myButton.grid(row=0, column=0, padx=10)
#Create clipboard Button
clip_button = Button(my_Frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)



root.mainloop()