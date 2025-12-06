import tkinter as tk
from datetime import date
from tkinter import messagebox

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        today = date.today()
        
        age = today.year - year - ((today.month, today.day) < (month, day))

        if age < 0 or age > 150:
            messagebox.showerror("Error", "Please check your date of birth.")
            result_label.config(text="Age: Invalid DOB", fg='red')
            return

        result_label.config(text=f"You are {age} years old!", fg='blue')

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers for Day, Month, and Year.")
        result_label.config(text="Age: Error", fg='red')

root = tk.Tk()
root.title("My Simple Age App")
root.geometry("250x300")
root.config(bg='lightyellow') 

tk.Label(root, text="Age Calculator", bg='lightyellow', font=('Arial', 14, 'bold')).pack(pady=10)

tk.Label(root, text="Enter Date of Birth:", bg='lightyellow').pack()

tk.Label(root, text="Day (DD)", bg='lightyellow').pack()
entry_day = tk.Entry(root, width=5)
entry_day.pack()

tk.Label(root, text="Month (MM)", bg='lightyellow').pack()
entry_month = tk.Entry(root, width=5)
entry_month.pack()

tk.Label(root, text="Year (YYYY)", bg='lightyellow').pack()
entry_year = tk.Entry(root, width=8)
entry_year.pack()

button_calc = tk.Button(root, text="Calculate", command=calculate_age, bg='green', fg='white')
button_calc.pack(pady=15)

result_label = tk.Label(root, text="Age: ", bg='lightyellow', font=('Arial', 12))
result_label.pack()

root.mainloop()