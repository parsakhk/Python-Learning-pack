from tkinter import *
Input = Tk()
Input.title("Calculator by tiky!")
#Entry of our calculator
e = Entry(Input, width=30, borderwidth=7)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def Button_click(number):
 
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def Button_clear():
    e.delete(0, END)

def Button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)
def Button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

def Button_minus():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)
def Button_devide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)
def Button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

#Buttons(100 Lines)
button1 = Button(Input, text="1", padx=40, pady=20, command= lambda: Button_click(1))
button2 = Button(Input, text="2", padx=40, pady=20, command= lambda: Button_click(2))
button3 = Button(Input, text="3", padx=40, pady=20, command= lambda: Button_click(3))
button4 = Button(Input, text="4", padx=40, pady=20, command= lambda: Button_click(4))
button5 = Button(Input, text="5", padx=40, pady=20, command= lambda: Button_click(5))
button6 = Button(Input, text="6", padx=40, pady=20, command= lambda: Button_click(6))
button7 = Button(Input, text="7", padx=40, pady=20, command= lambda: Button_click(7))
button8 = Button(Input, text="8", padx=40, pady=20, command= lambda: Button_click(8))
button9 = Button(Input, text="9", padx=40, pady=20, command= lambda: Button_click(9))
button0 = Button(Input, text="0", padx=40, pady=20, command= lambda: Button_click(0))
button_add = Button(Input, text="+", padx=39, pady=20, command=Button_add)
button_equal = Button(Input, text="=", padx=91, pady=20, command=Button_equal)
button_clear = Button(Input, text="Clear", padx=79, pady=20, command=Button_clear)
button_minus = Button(Input, text="-", padx=41, pady=20, command=Button_minus)
button_devide = Button(Input, text="/", padx=40, pady=20, command=Button_devide)
button_multiply = Button(Input, text="*", padx=40, pady=20, command=Button_multiply)
#Grid our buttons
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_minus.grid(row=6, column=0)
button_devide.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)


Input.mainloop()