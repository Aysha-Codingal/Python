from tkinter import *
from datetime import date

root = Tk()
root.title("My First Window")
root.geometry("400x300")
root.configure(bg='magenta')

def greet():
    name = entry1.get()
    dt = date.today()
    g = "welcome " + name + "\nToday's date is " + str(dt)
    text1.delete("1.0","end")
    text1.insert("1.0",g)
f = ("Times",20,'bold')
label1 = Label(root,text = "Name ", bg = 'magenta', fg ='black',font=f)
label1.pack(pady=10)
entry1 = Entry(root)
entry1.pack(pady=10)
button1 = Button(root,text = "begin",bg = 'black',fg = 'magenta',command = greet,font=f)
button1.pack(pady=10)

text1 = Text(root,fg='black',bg= 'beige',width = 40,height=10,font=f)
text1.pack(pady=10)
root.mainloop()
