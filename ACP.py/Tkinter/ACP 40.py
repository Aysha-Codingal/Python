from tkinter import *
from tkinter import messagebox
import re 

root = Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False) 

def check_strength(event=None):
    password = password_entry.get()
    
    strength_label.config(text="", bg=root.cget('bg'))
    
    length = len(password)
    strength = "Very Weak"
    color = "red"
    
    if length == 0:
        strength = "Please Enter a Password"
        color = "lightgrey"
        
    elif length >= 12:
        strength = "Strong"
        color = "green"
        
    elif length >= 8:
        strength = "Moderate"
        color = "orange"
        
    elif length >= 4:
        strength = "Weak"
        color = "yellow"
        
    strength_label.config(text=strength, bg=color, fg="black", font=('Arial', 12, 'bold'))


title_label = Label(root, text="Enter Password to Check Strength:", font=('Arial', 14))
title_label.pack(pady=10)

password_entry = Entry(root, width=30, show="*", font=('Arial', 12))
password_entry.bind("<KeyRelease>", check_strength)
password_entry.pack(pady=5)

strength_label = Label(root, text="Start Typing...", font=('Arial', 12, 'bold'), padx=10, pady=5)
strength_label.pack(pady=20)

root.mainloop()