from tkinter import *
from datetime import datetime
import random
root = Tk()
root.title("RESTARUANT MANAGEMENT SYSTEM")
root.geometry("800x400")
root.configure(bg='beige')
frame1 = Frame(root, width = 500, height = 300, relief= SUNKEN, bg = 'beige')
frame1.pack()
label1 = Label(frame1,font=("arial",18,'bold'),text="Restaurant Management System",bg = "beige", fg = "firebrick")
label1.grid(row = 0,column=0,columnspan=4,padx=10,pady=10)

drink = StringVar()
pizza = StringVar()
fries = StringVar()
burger = StringVar()
largeburger = StringVar()

labeldrink = Label(frame1,font=("arial",18,'bold'),text="Drink",bg = "beige", fg = "firebrick")
labeldrink.grid(row = 3,column=0,padx=10,pady=10)
enterydrink = Entry(frame1,textvariable=drink,justify=RIGHT)
enterydrink.grid(row = 3, column =1,padx=10,pady=10)
enterydrink.insert(END,0)

labelpizza = Label(frame1,font=("arial",18,'bold'),text="Pizza",bg = "beige", fg = "firebrick")
labelpizza.grid(row = 4,column=0,padx=10,pady=10)
enterypizza = Entry(frame1,textvariable=pizza,justify=RIGHT)
enterypizza.grid(row = 4, column =1,padx=10,pady=10)
enterypizza.insert(END,0)


labelburger = Label(frame1,font=("arial",18,'bold'),text="Burger",bg = "beige", fg = "firebrick")
labelburger.grid(row = 5,column=0,padx=10,pady=10)
enteryburger = Entry(frame1,textvariable=burger,justify=RIGHT)
enteryburger.grid(row = 5, column =1,padx=10,pady=10)
enteryburger.insert(END,0)

labellargeburger = Label(frame1,font=("arial",18,'bold'),text="LargeBurger",bg = "beige", fg = "firebrick")
labellargeburger.grid(row = 6,column=0,padx=10,pady=10)
enterylargeburger = Entry(frame1,textvariable=largeburger,justify=RIGHT)
enterylargeburger.grid(row = 6, column =1,padx=10,pady=10)
enterylargeburger.insert(END,0)

labelfries = Label(frame1,font=("arial",18,'bold'),text="Fries",bg = "beige", fg = "firebrick")
labelfries.grid(row = 7,column=0,padx=10,pady=10)
enteryfries = Entry(frame1,textvariable=fries,justify=RIGHT)
enteryfries.grid(row = 7, column =1,padx=10,pady=10)
enteryfries.insert(END,0)


labelorderno = Label(frame1,font=("Times",18,'bold'),text="Orderno",bg = "beige", fg = "firebrick")
labelorderno.grid(row = 3,column=2,padx=10,pady=10)
enteryorderno = Entry(frame1)
enteryorderno.grid(row = 3, column =3,padx=10,pady=10)
enteryorderno.insert(END,0)

labelcost = Label(frame1,font=("arial",18,'bold'),text="Cost",bg = "beige", fg = "firebrick")
labelcost.grid(row = 4,column=2,padx=10,pady=10)
enterycost = Entry(frame1)
enterycost.grid(row = 4, column =3,padx=10,pady=10)
enterycost.insert(END,0)


labelservice = Label(frame1,font=("arial",18,'bold'),text="Service Charge",bg = "beige", fg = "firebrick")
labelservice.grid(row = 5,column=2,padx=10,pady=10)
enteryservice = Entry(frame1)
enteryservice.grid(row = 5, column =3,padx=10,pady=10)
enteryservice.insert(END,0)

labeltax = Label(frame1,font=("arial",18,'bold'),text="Tax",bg = "beige", fg = "firebrick")
labeltax.grid(row = 6,column=2,padx=10,pady=10)
enterytax = Entry(frame1)
enterytax.grid(row = 6, column =3,padx=10,pady=10)
enterytax.insert(END,0)

labeltotal = Label(frame1,font=("arial",18,'bold'),text="Total",bg = "beige", fg = "firebrick")
labeltotal.grid(row = 7,column=2,padx=10,pady=10)
enterytotal = Entry(frame1,)
enterytotal.grid(row = 7, column =3,padx=10,pady=10)
enterytotal.insert(END,0)


#----------------------------------------------------------------------------------------------------------------
def ex():
    root.destroy()
def reset():
    enterydrink.delete(0,END)    
    enterydrink.insert(END,0)

    enterypizza.delete(0,END)    
    enterypizza.insert(END,0)
    enteryburger.delete(0,END)    
    enteryburger.insert(END,0)
    enterylargeburger.delete(0,END)    
    enterylargeburger.insert(END,0)
    enteryfries.delete(0,END)    
    enteryfries.insert(END,0)
    enteryorderno.delete(0,END)    
    enteryorderno.insert(END,0)
    enterytax.delete(0,END)    
    enterytax.insert(END,0)
    enterycost.delete(0,END)    
    enterycost.insert(END,0)
    enterytotal.delete(0,END)    
    enterytotal.insert(END,0)




button1 = Button(frame1,font=("arial",18,'bold'),text="PRICE",bg = "beige", fg = "firebrick")
button1.grid(row = 10,column=0,padx=10,pady=10)
button2 = Button(frame1,font=("arial",18,'bold'),text="TOTAL",bg = "beige", fg = "firebrick")
button2.grid(row = 10,column=1,padx=10,pady=10)
button3 = Button(frame1,font=("arial",18,'bold'),text="RESET",bg = "beige", fg = "firebrick", command=reset)
button3.grid(row = 10,column=2,padx=10,pady=10)
button4 = Button(frame1,font=("arial",18,'bold'),text="EXIT",bg = "beige", fg = "firebrick", command=ex)
button4.grid(row = 10,column=3,padx=10,pady=10)



































root.mainloop()