import tkinter as tk
from tkinter import *

r = 0 # row
c = 0 # column

root = tk.Tk()
root.config(bg= 'light blue')
canvas = Canvas(root, height = 600, width = 600, relief = RAISED, bg = 'gray',bd = 13)
canvas.grid(row = 7, column = 0, columnspan = 3 )

def poo():
    pass

coco = Button(root, relief=RIDGE,bg='light gray', text='coco', command = poo)
coco.grid(row=0,column=0)

straw= Button(root, relief=RIDGE,bg='light gray', text='strawberry', command = poo)
straw.grid(row=0,column=1)

van = Button(root, relief=RIDGE,bg='light gray', text='vanilla', command = poo)
van.grid(row=0,column=2)
items ={'coco': '1.00', 'vanilla': '1.25', 'strawberry': '1.50'}

root.mainloop()