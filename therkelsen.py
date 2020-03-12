import tkinter as tk
from tkinter import *

r = 0 # row
c = 0 # column
scoops= 0
circles = []
root = tk.Tk()
root.config(bg= 'light blue')
canvas = Canvas(root, height =650, width = 600, relief = RAISED, bg = 'gray',bd = 13)
canvas.grid(row = 2, column = 0, columnspan = 3 )
canvas.create_polygon(300,650,350,500,250,500, fill='#b5651d')
colors ={'coco': 'brown', 'vanilla': 'white', 'strawberry': 'pink'}
totalAm = 0

def poo(flavor):
    global scoops
    global circles
    global totalAm
    color = colors[flavor]
    if scoops < 3:
        global coords
        lb.delete(END)
        circles.append(canvas.create_oval(coords, fill=color))
        canvas.lower(circles[-1])
        coords[1] -= 30
        coords[3] -= 30
        scoops += 1
        price = items[flavor]
        totalAm += float(price)
        lb.insert(END, '{} for {}'.format(flavor, price))
        lb.insert(END, 'Total: {}'.format(round(totalAm,2)))
    else:
        pass

def restart():
    global circles
    global totalAm
    global scoops
    global coords
    for x in circles:
        canvas.delete(x)
        circles =[]
    scoops = 0
    coords = [250, 450, 350, 550]
    lb.delete(2, END)
    lb.insert(END, ' ')
    totalAm = 0

coords = [250, 450, 350, 550]
coco = Button(root, relief=RIDGE,bg='light gray', text='coco', command = lambda: poo('coco'))
coco.grid(row=0,column=0)

straw= Button(root, relief=RIDGE,bg='light gray', text='strawberry', command = lambda: poo('strawberry'))
straw.grid(row=0,column=1)

van = Button(root, relief=RIDGE,bg='light gray', text='vanilla', command = lambda: poo('vanilla'))
van.grid(row=0,column=2)
items ={'coco': '1.00', 'vanilla': '1.25', 'strawberry': '1.50'}

reset= Button(root,relief=RIDGE,bg='light gray', text='Remove', command = restart)
reset.grid(row=3)

lb = Listbox(root)
lb.grid(row = 2, column = 4)
lb.insert(END, 'Ice Cream')
lb.insert(END, '-'*30)
lb.insert(END,'')

root.mainloop()
