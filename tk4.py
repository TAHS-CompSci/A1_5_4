import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

#Classes
class Substance():
    """
    A class for defining all the buttons
    """
    def __init__(self,root,r,c,food, pay):
        self.food = food.title()
        self.pay = pay
        self.thing = Button(bg='tan',bd=4,fg='blue',relief = GROOVE,text='{} for ${}'.format(food.title(),pay),command = lambda:[self.receipt(),self.addObject()])
        self.thing.grid(row = r,column = c)
        self.photo = tk.PhotoImage(file = food +'.gif')
    def receipt(self):
        """
        This Function Does all the math for the receipt, and adds on to the receipt.
        """
        global taxr
        global sub
        lb.insert(END,'{}      ${}'.format(self.food,self.pay))
        lb.insert(END,'-'*30) # Creates top of receipt
        lb.see(END)
        sub = round(float(sub)+ float(self.pay),2)
        taxAm = round(float(sub)*float(taxr),2)
        totalAm=round(float(sub)+float(taxAm),2)
        tax.config(text='Total Tax  ${}'.format(taxAm))
        subtotal.config(text='Subtotal  ${}'.format(sub))
        total.config(text='Total  ${}'.format(totalAm))

    def addObject(self):
        img = canvas.create_image(random.randint(20,600),random.randint(20,600),image=self.photo)
        shapes.append(img)
        shapes.append('linebreak')
    


#Functions
def delete():
    """
    A Function that will handle a situation where a customer decides to remove an item
    """
    global sub
    global taxr
    item = lb.curselection()
    food = lb.get(ACTIVE)
    food = food[0:len(food)-11]
    canvas.delete(shapes[item[0]])
    if lb.index(item) % 2 == 1:
        lb.delete(item)
        lb.insert(item,'Removed')
        for item in items:
            for x,y in item.items():
                if x.title() == food:
                    sub = round(float(sub)-float(y),2)
                    taxAm= round(float(sub)*float(taxr),2)
                    totalAm = round(float(sub)+float(taxAm),2)
                    tax.config(text='Total Tax  ${}'.format(taxAm))
                    subtotal.config(text='Subtotal  ${}'.format(sub))
                    total.config(text='Total  ${}'.format(totalAm))


root = tk.Tk(className='Concession Stand')
root.config(bg='salmon')

#variables
categ = ['Food','Bevarage','Candy'] # Categories
r = 0 # row
c = 0 # column
sub = 0.00 # subtotal money
taxr = 0.04 # tax rate 4 %
items = [{'popcorn':'3.25','Hot Dogs':'2.00','pretzel':'1.00','Nachos':'3.00','pickle': '1.00','pizza':'2.00'},{'pepsi':'1.00','sprite':'1.00','root beer':'1.00'},{'butterfinger':'1.00','Laffy Taffy':'0.98','heath':'1.00'}]
shapes = ['linebreak']

#canvas
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='gray',bd=13)
canvas.grid(row=7, column=0,columnspan=3)

#Receipt
root3= tk.Tk(className = 'receipt')
root3.config(bg = 'light gray')
lb = Listbox(root3) 
lb.insert(END,'    -concession stand-')
lb.grid(row = 1,column = 0,columnspan = 4)

#other misc items
delButt = Button(root3,relief=RIDGE,bg='light gray',text = 'Remove Selected',command = delete)
delButt.grid(row=0,column=0)

#Categories
for item in items:
  categName = categ[items.index(item)]
  categLabel = Label(text = categName,bg = 'salmon')
  categLabel.grid(row = r,column = c)
  for key,value in item.items():
    r += 1
    thing = Substance(root,r,c,key,value)
  r = 0
  c += 1

  
#Money Portion
subtotal = Label(root3,relief=RAISED,bg='light gray',text = 'Subtotal  $0.00')
subtotal.grid(row = 2,column = 0)
tax = Label(root3,relief=RAISED,bg='light gray',text = 'Total Tax  $0.00')
tax.grid(row = 3,column = 0)
total = Label(root3,relief = RAISED,bg='light gray',text = 'Total  $0.00')
total.grid(row = 4,column = 0)
