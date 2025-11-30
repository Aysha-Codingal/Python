from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Event Handler")
window.geometry("300x300")

def alert():
    messagebox.showwarning("ALERT!!!","VIRUS FOUND!")

button1 = Button(text = "Scan for Virus",command= alert)    
button1.place(x=150,y=150)

window.mainloop()