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

Ice_Cream_Sizes_Prices = {'Single': 1.50, 'Double': 2.50, 'Triple': 3.50}
print (Ice_Cream_Sizes_Prices)  

  global taxr
        global sub
        lb.insert(END,'{}      ${}'.format(self.Ice_Cream,self.pay))
        lb.insert(END,'-'*30) 
        lb.see(END)
        sub = round(float(sub)+ float(self.pay),2)
        taxAm = round(float(sub)*float(taxr),2)
        totalAm=round(float(sub)+float(taxAm),2)
        tax.config(text='Total Tax  ${}'.format(taxAm))
        subtotal.config(text='Subtotal  ${}'.format(sub))
        total.config(text='Total  ${}'.format(totalAm))

        def delete():
   
    global sub
    global taxr
    item = lb.curselection()
    Ice_Cream = lb.get(ACTIVE)
    Ice_cream = Ice_Cream[0:len(Ice_Cream)-11]
    canvas.delete(shapes[item[0]])
    if lb.index(item) % 2 == 1:
    lb.delete(item)
    lb.insert(item,'Removed')
    for item in items.keys():
    for x,y in items[item].items():
    if x.title() == food:
    sub = round(float(sub)-float(y),2)
    taxAm= round(float(sub)*float(taxr),2)
    totalAm = round(float(sub)+float(taxAm),2)
    tax.config(text='Total Tax  ${}'.format(taxAm))
    subtotal.config(text='Subtotal  ${}'.format(sub))
    total.config(text='Total  ${}'.format(totalAm))


root = tk.Tk(className='Ice Cream Stand')
root.config(bg='Ice Cream')

r = 0 
c = 0 
sub = 0.00 
taxr = 0.75
items = {'Ice Cream'{'Single':1.50, 'Double': 2.50, 'Triple':3.50}

        