import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile    

def open_file():
    file = askopenfile(mode = 'r',filetypes = [('text file','*.txt')])
    if file is not None:
        content = file.read()
        text1.delete("1.0","end")
        text1.insert(END,content)
    file.close()    

def save_file():
    file = asksaveasfile(mode = 'w',filetypes = [('text files','*.txt')])    
    if file is not None:
        mytext1 = text1.get("1.0",END)
        file.write(mytext1)
    file.close()    

window = Tk()
window.title("Text editor")
window.geometry("500x400")
window.configure(bg = 'skyblue')
text1 = Text(window, width= 50, height = 20, relief = 'sunken',bd = 3)
button1 = Button( window, text = 'open' ,width = 10, height = 1,command=open_file)
button2 = Button( window, text = 'Save' , width = 10, height = 1,command=save_file)
button1.grid(row = 1, column = 0)
button2.grid(row = 2, column = 0)
text1.grid(row = 1, column = 1, rowspan = 2, pady = 10, padx = 10)
window.mainloop()