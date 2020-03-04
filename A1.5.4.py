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
    self.food = food
    self.pay = pay
    self.thing = Button(text='{} for ${}'.format(food,pay),command = self.receipt, bg='white')
    self.thing.grid(row = r,column = c)
    self.photo = tk.PhotoImage(file = food +'.gif')

  def receipt(self):
    """
    This Function Does all the math for the receipt, and adds on to the receipt.
    """
    global taxr
    global sub
    lb.insert(END,'{}      ${}'.format(self.food,self.pay))
    lb.insert(END,'-'*30) # Creates top of receipt
    lb.see(END)
    sub = round(float(sub)+ float(self.pay),2)
    taxAm = round(float(sub)*float(taxr),2)
    totalAm=round(float(sub)+float(taxAm),2)
    tax.config(text='Total Tax  ${}'.format(taxAm))
    subtotal.config(text='Subtotal  ${}'.format(sub))
    total.config(text='Total  ${}'.format(totalAm))

  def addImage(self):
    img=canvas.create_image(random.randint(20,600),random.randint(20.600),image=self.photo)
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
  if lb.index(item) % 2 == 1:
    lb.delete(item)
    lb.insert(item,'Removed')
    for item in items:
      for x,y in item.items():
        if x == food:
          sub = round(float(sub)-float(y),2)
          taxAm= round(float(sub)*float(taxr),2)
          totalAm = round(float(sub)+float(taxAm),2)
          tax.config(text='Total Tax  ${}'.format(taxAm))
          subtotal.config(text='Subtotal  ${}'.format(sub))
          total.config(text='Total  ${}'.format(totalAm))


def about():
  tk.messagebox.showinfo('About','A Concession Stand for A1.5.4 in CSP')


root = tk.Tk()
root.config(bg='salmon')
#variables
categ = ['Food','Bevarage','Candy'] # Categories
r = 0 # row
c = 0 # column
sub = 0.00 # subtotal money
taxr = 0.04 # tax rate 4 %
items = [{'Hot Dogs':'2.00','Pretel':'1.00','Nachos':'3.00','Pickle': '1.00','Pizza':'2.00'},{'Pepsi':'1.00','Sprite':'1.00','Root Beer':'1.00'},{'Butterfinger':'1.00','Laffy_Taffy':'0.98','Heath':'1.00'}]
shapes=['linebreak']
#canvas
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='grey')
canvas.grid(row=6, column=0,columnspan=3)

#Receipt
root3= tk.Tk()
lb = Listbox(root3) 
lb.insert(END,'    -Concession Stand-')
lb.grid(row = 6,column = 4,columnspan = 3)

#other misc items
delButt = Button(root3,text = 'Remove Selected', command = delete, bg='red')
delButt.grid(row=5,column = 4)

#Categories
for item in items:
  categName = categ[items.index(item)]
  categLabel = Label(text = categName, bg='salmon' )
  categLabel.grid(row = r,column = c)
  for key,value in item.items():
    r += 1
    thing = Substance(root,r,c,key,value)
  r = 0
  c += 1

  
#Money Portion
subtotal = Label(root3,text = 'Subtotal  $0.00')
subtotal.grid(row = 1,column = 3)
tax = Label(root3,text = 'Total Tax  $0.00')
tax.grid(row = 2,column = 3)
total = Label(root3,text = 'Total  $0.00')
total.grid(row = 3,column = 3)


#menu
menu = Menu(root3) 
root.config(menu= menu) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help',menu = helpmenu)
helpmenu.add_command(label='About',command = about)
helpmenu.add_command(label='Quit', command=root.quit) 
root.mainloop()