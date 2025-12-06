import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        inches = float(entry_inches.get())
        
        centimeters = inches * 2.54
        
        result_label.config(text=f"Result: {centimeters:.2f} cm", fg='darkgreen')
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
        result_label.config(text="Result: Error", fg='red')

root = tk.Tk()
root.title("Inches to CM Converter")
root.geometry("300x180")
root.config(bg='lightgrey')


tk.Label(root, text="Enter Length in Inches:", bg='lightgrey').pack(pady=10)

entry_inches = tk.Entry(root, width=15)
entry_inches.pack()

button_convert = tk.Button(root, 
        text="Convert",
        command=convert, 
        bg='blue', 
        fg='white')
button_convert.pack(pady=15)

result_label = tk.Label(root, text="Result: ", bg='lightgrey', font=('Arial', 12, 'bold'))
result_label.pack()

root.mainloop()