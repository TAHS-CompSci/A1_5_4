"""
1.5.4 design a gui
Myamoto
ice cream shop gui
"""



from tkinter import * 

root = Tk()
root.geometry('500x500')

c = Canvas(root, height=400, width=500)

b = Button(root, width = 20)
b.pack()


root.mainloop()