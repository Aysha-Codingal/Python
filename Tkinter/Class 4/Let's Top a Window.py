from tkinter import *

root = Tk()
root.title("The main window")
root.geometry("500x500")
root.configure(bg = 'palevioletred')

def top():
    wtop =Toplevel()
    wtop.title("Toplevel window")
    wtop.geometry("200x200")
    wtop.configure (bg="Burlywood")
    label2 = Label(root, text = "this is the top level window")
    label2.pack(pady= 20)
    wtop.mainloop()

label1 = Label(root, text = "this is the Main window")
label1.pack(pady= 20)
button1 = Button(root, text = "Click Me", command = top)
button1.pack(pady=20)
root.mainloop()