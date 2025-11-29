from tkinter import *
from datetime import date

root = Tk()
root.title("LOGIN APP")
root.geometry("450x400")
root.configure(bg = 'grey')
def login():
    name = entry1.get()
    g = "WELCOME" +     name + "\n YOU HAVE SUCCESSFULLY LOGGED IN"
    text1.delete("1.0","end")
    text1.insert("1.0",g)
frame1 = Frame(root,bg = 'thistle',width = 300,height=350,relief='sunken',bd=3)    
frame1.pack()
label1 = Label(frame1,text = "Name", bg="mediumpurple",fg= 'black')
label1.pack(pady=7)
entry1 = Entry(frame1)
entry1.pack(pady=5)
label2 = Label(frame1,text = "PASSWORD",bg="mediumpurple",fg = 'black')
label2.pack(pady=5)
entry2 = Entry(frame1,show= "*")
entry2.pack(pady=5)
button1 = Button(frame1,text = "Login",bg="red",fg= 'black',command = login)
button1.pack(pady=5)
text1 = Text(root, bg = "burlywood",fg = 'brown',width = 50,height = 10)
text1.pack()

root.mainloop()
