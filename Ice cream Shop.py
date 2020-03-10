import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
button = Button(root, text='click me.')
button.grid(row=0, column=0)
# creates the canvas 
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='Pink')
canvas.grid()

drawpad = Canvas(root,height=600,width=300, background ='white')
drawpad.grid(row=1, column=2)
radio = [0]*4 # create a list
data = IntVar()
for i in range(4):
    radio[i] = Radiobutton(root, text=str(i),
                           variable=data, value=i)
    radio[i].grid(row=i,column=2)
data.set(3)
root.mainloop()