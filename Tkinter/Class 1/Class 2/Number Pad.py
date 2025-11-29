from tkinter import *
from datetime import date

root = Tk()
root.title("number pad")
root.geometry("250x300")
root.configure(bg='beige')
t = [[7,8,9],[4,5,6],[1,2,3],['0','#','*']]

for i in range (4):
    root.rowconfigure(i,weight = 0,minsize=70)
    for j in range(3):
        root.columnconfigure(j,weight = 0,minsize=80)
        label1 = Label(root,text = t[i][j], bg = 'deepskyblue',fg = 'black',width=4,relief='sunken')
        label1.grid(row= i,column = j)

root.mainloop()        