import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

#Classes
class Window():
    """
    Create Category Windows and call substance
    """
    def __init__(self,name,items,r,c):
        self.root = tk.Tk(className = name)
        for key,value in items.items():
            thing = Substance(self.root,r,c,key,value)
            r += 1
            if r == 11:
                r = 0
                c += 1
        self.root.withdraw()
    def show(self):
        self.root.deiconify()
        
        
class Substance():
    """
    A class for defining all the buttons
    """
    def __init__(self,root,r,c,food, pay):
        self.food = food.title()
        self.pay = pay
        self.root = root
        self.thing = Button(self.root,bg='tan',bd=4,fg='blue',relief = GROOVE,text='{} for ${}'.format(food.title(),pay),command = lambda:[self.receipt(),self.addObject()])
        self.thing.grid(row = r,column = c)
        try:
            self.photo = tk.PhotoImage(file = food +'.gif')
        except:
            self.photo = tk.PhotoImage(file = 'pizza.gif')
   
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
        """ 
        Create images on canvas
        """
        print(shapes)
        img = canvas.create_image(random.randint(20,600),random.randint(20,600),image=self.photo)
        shapes.append(img)
        shapes.append('linebreak')
        self.root.withdraw()
    


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
        for item in items.keys():
            for x,y in items[item].items():
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
r = 0 # row
c = 0 # column
sub = 0.00 # subtotal money
taxr = 0.075 # tax rate
items = {'Food':{'popcorn':'3.25','Hot Dogs':'2.00','pretzel':'1.00','Nachos':'3.00','pickle': '1.00','pizza':'2.00'},'Beverage':{'Pepsi':'1.00','Sprite':'1.00','Root Beer':'1.00', 'Pepsi':'1.00','Sprite':'1.00', 'Root Bear':'1.00', 'Mtn. Dew':'1.00', 'Dr. pepper.':'1.00', 'Extra pibb':'2.00', 'Coca Cola':'1.00', 'Fanta Orange':'2.00', 'Mellow Yellow':'2.00', 'Crush':'1.00', '7-Up':'1.00', 'Diet Coke':'1.50', 'Diet mtn dew':'1.50', 'Diet pepsi':'1.50', '7 up cherry':'2.00', 'A&W cream soda':'1.75', 'Sun Drop':'2.00', 'Squirt':'2.00', 'Fanta Grape':'2.00', 'Water':'0.75', 'Lemonade':'1.30'},'Candy':{'Butterfinger':'1.00','Laffy Taffy':'0.98','Heath':'1.00', 'Hershey': '1.73', 'Skittles':'2.00', 'M&Ms' :'$2.00', 'Kit Kat' :'1.73', 'Ring pop':'1.89','Push pop':'1.89','Snickers':'1.73','Milky Way':'1.54','Twix':'1.73','Almound Joy':'$1.78','3 Musketeers':'1.78','Baby Ruth':'1.89', 'Mounds':'1.89','100 Grand Bar':'1.89','Crunch':'1.73','Payday':'1.89','Reeses Cups':'2.00', 'Sour patch kids':'2.34','Starburst':'2.15'}}
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
for item in items.keys():
    name = item
    cax = Window(name,items[item],r,c)
    categA = Button(text = item,bg = 'salmon',command = cax.show)
    categA.grid(row = 0,column = c)
    c += 1
c = 0

  
#Money Portion
subtotal = Label(root3,relief=RAISED,bg='light gray',text = 'Subtotal  $0.00')
subtotal.grid(row = 2,column = 0)
tax = Label(root3,relief=RAISED,bg='light gray',text = 'Total Tax  $0.00')
tax.grid(row = 3,column = 0)
total = Label(root3,relief = RAISED,bg='light gray',text = 'Total  $0.00')
total.grid(row = 4,column = 0)
    
root.mainloop()
