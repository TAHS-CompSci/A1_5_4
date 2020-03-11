import tkinter as tk
from tkinter import *

root = tk.Tk(className = 'ice cream')
root.config(bg = 'salmon',width = 800, height = 800)

def addShape(flavor):
	global shapes
	global cost
	receipt.delete(END)
	amount = scoop.get()
	opt = {'Vanilla':'white','Strawberry':'pink','Chocolate':'brown'}
	color = opt[flavor]
	cost += price[flavor] * amount
	for x in range(amount):
		shape = c.create_oval(coords, fill = color)
		shapes.append(shape)
		coords[1] -= 60
		coords[3] -= 60
		c.lower(shape)
	receipt.insert(END, '{}x {} for ${}.00'.format(amount,flavor, price[flavor] * amount))
	receipt.insert(END, 'Total: ${}.00'.format(cost))
	receipt.see(END)

def reset():
	global shapes
	global coords
	global cost
	for x in shapes:
		c.delete(x)
	shapes = []
	cost = 0
	receipt.delete(2,END)
	coords = [300,560,500,430]	
	receipt.insert(END, '')

cost = 0
scoopDict = {'One Scoop':1,'Two Scoop':2,'Three Scoop':3}
price = {'Vanilla': 1,'Strawberry': 2,'Chocolate': 2}
coords = [300,560,500,430]	
shapes = []
c = Canvas(root, width = 800, height = 800, bg = 'tan', bd = 8, relief = GROOVE)
c.grid(row = 2)
ff = Frame(root)
ff.grid()
sf = Frame(root)
sf.grid(row = 1)
scoop = IntVar()
scoop.set(1)
col = 1

c.create_polygon(300,520,400,820,500,520,fill = '#c78330')
c.lower(c.create_oval(300,510,500,530,fill = '#c78330'))
receipt = Listbox(root, bd = 7, relief = RIDGE)
receipt.insert(END, 'Ice Cream')
receipt.insert(END,'-'*30)
receipt.insert(END, '')
receipt.grid(row = 4, columnspan = 3)

confirm = Button(root, activebackground = 'dark grey', bg = 'grey', bd = 6, relief = SUNKEN, text = 'Confirm', command = reset)
confirm.grid(row = 5)

van = Button(ff, activebackground = 'tan', fg = 'gray', bg = 'white', bd = 7, relief = RAISED, text = 'Vanilla', command = lambda: addShape('Vanilla'))
van.grid(column = 0)

straw = Button(ff, activebackground = 'tan', fg = 'red', bg = 'pink', bd = 7, relief = RAISED, text = 'Strawberry', command = lambda: addShape('Strawberry'))
straw.grid(row = 0, column = 1)

choc = Button(ff, activebackground = 'tan', bg = 'brown', fg = 'tan', bd = 7, relief = RAISED, text = 'Chocolate', command = lambda: addShape('Chocolate'))
choc.grid(row = 0, column = 2)

for x,y in scoopDict.items():
	b = Radiobutton(sf, activebackground = 'dark grey', bg = 'gray', bd = 5, relief = SUNKEN, text = x, variable = scoop, value = y)
	b.grid(row = 8,column = col)
	col += 1

root.mainloop()