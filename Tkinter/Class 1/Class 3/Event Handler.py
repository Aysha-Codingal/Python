from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("300x300")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>",handle_keypress)

def handle_click(event):
    print("\n The button was clicked")

button1 = Button(text = "click me")    
button1.place(x=150,y=150)

button1.bind("<Button-1>",handle_click)

window.mainloop()