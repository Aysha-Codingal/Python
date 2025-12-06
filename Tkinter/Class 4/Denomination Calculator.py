from tkinter import *
from tkinter import messagebox
from os import system
system("pip install pillow")
#from PIL import Image, ImageTk
root = Tk()
root.title("DENOMINATION CALCULATOR")
root.geometry("600x600")
#upload = Image.open("app_img.jpg")
#upload = upload.resize((300,300))
#img = ImageTk.PhotoImage(upload)

#label1 = Label(root,Image=img)

label1 = Label(root, text = "HEY USER! WELCOME TO THE DENOMINATION CALCULATOR APPLICATION")
label1.place(x= 20, y= 320)


def msg():
    msgbox = messagebox.showinfo("ALERT", "DO YOU WANT TO CALCULATE THE DENOMINATION COUNT ?")
    if msgbox == 'ok':
        topwin()
button1 = Button (root, text="~ LET'S GET STARTED ~",command=msg,bg='brown',fg='white')       
button1.place(x=180, y=370)

def topwin():
    def calculator():
        global amount
        amount = int(entryt.get())
        note2000 = amount//2000
        note500 = (amount%2000)//500
        note100 = ((amount%2000)%500)//100

        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
    top = Toplevel()        
    top.title("toplevel")
    top.geometry("500x500")
    labelt = Label(top,text = "ENTER THE TOTAL AMOUNT")
    labelt.place(x=20, y=10) 
    entryt = Entry(top)
    entryt.place(x = 20, y = 40)
    lb1 = Label(top, text = "HERE ARE THE NUMBER OF THE NOTES FOR EACH")
    lb1.place(x=50,y=100)
    l1 = Label(top,text = "2000")
    l2 = Label(top,text = "500")
    l3 = Label(top,text = "100")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry (top)
    btn = Button(top,text='calculate',command=calculator)

    btn.place(x=150,y = 120)
    l1.place(x = 100,y = 200)
    l2.place(x = 100,y = 230)
    l3.place(x = 100,y = 250)
    t1.place(x=200, y = 200)
    t2.place(x=200, y = 230)
    t3.place(x=200, y = 250)


root.mainloop()




