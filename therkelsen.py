import tkinter as tk
from tkinter import *

r = 0 # row
c = 0 # column

root = tk.Tk()
root.config(bg= 'light blue')
canvas = Canvas(root, height =650, width = 600, relief = RAISED, bg = 'gray',bd = 13)
canvas.grid(row = 2, column = 0, columnspan = 3 )
canvas.create_polygon(300,650,350,500,250,500, fill='#b5651d')

def poo(flavor):
    global coords
    circles = []
    circles.append(canvas.create_oval(coords, fill=flavor))
    coords[1] -= 30
    coords[3] -= 30


coords = [250, 450, 350, 550]
coco = Button(root, relief=RIDGE,bg='light gray', text='coco', command = lambda: poo('brown'))
coco.grid(row=0,column=0)

straw= Button(root, relief=RIDGE,bg='light gray', text='strawberry', command = lambda: poo('pink'))
straw.grid(row=0,column=1)

van = Button(root, relief=RIDGE,bg='light gray', text='vanilla', command = lambda: poo('white'))
van.grid(row=0,column=2)
items ={'coco': '1.00', 'vanilla': '1.25', 'strawberry': '1.50'}



root.mainloop()
