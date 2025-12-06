import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        product = num1 * num2

        result_label.config(text=f"Product: {product}", fg='green')
    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only.")
        result_label.config(text="Product: Error", fg='red')

root = tk.Tk()
root.title("Simple Multiplier")
root.geometry("300x200")
root.config(bg='lightblue')

label_num1 = tk.Label(root, text="First Number:", bg='lightblue')
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=2)

label_num2 = tk.Label(root, text="Second Number:", bg='lightblue')
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=2)

button_calc = tk.Button(root, text="Calculate", command=calculate_product, bg='blue', fg='white')
button_calc.pack(pady=10)

result_label = tk.Label(root, text="Product: ", bg='lightblue', font=('Arial', 12, 'bold'))
result_label.pack(pady=5)

root.mainloop()