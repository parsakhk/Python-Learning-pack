from tkinter import *

root = Tk()
root.title("Canvas")
root.geometry("400x400")

canvas = Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=20)

#For creating a line
canvas.create_line(0, 100, 300, 100, fill="powder blue")
canvas.create_line(150, 0, 150, 200, fill="powder blue")

root.mainloop()