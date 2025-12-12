from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg='#f0f0f0')

user_choice_var = StringVar()
computer_choice_var = StringVar()
result_var = StringVar()

user_choice_var.set("?")
computer_choice_var.set("?")
result_var.set("Make your move!")

def play_game(user_input):
    user_choice_var.set(user_input)
    
    choices = ["Rock", "Paper", "Scissors"]
    computer_input = random.choice(choices)
    computer_choice_var.set(computer_input)
    
    result = ""
    
    if user_input == computer_input:
        result = "It's a Tie!"
    elif (user_input == "Rock" and computer_input == "Scissors") or \
         (user_input == "Paper" and computer_input == "Rock") or \
         (user_input == "Scissors" and computer_input == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
        
    result_var.set(result)

Label(root, text="Rock Paper Scissors", font=('Arial', 20, 'bold'), bg='#f0f0f0').pack(pady=10)

choice_frame = Frame(root, bg='#f0f0f0')
choice_frame.pack(pady=10)

Label(choice_frame, text="Your Move:", font=('Arial', 14), bg='#f0f0f0').grid(row=0, column=0, padx=20)
Label(choice_frame, textvariable=user_choice_var, font=('Arial', 24, 'bold'), fg='blue', bg='#f0f0f0').grid(row=1, column=0, padx=20)

Label(choice_frame, text="vs", font=('Arial', 18), bg='#f0f0f0').grid(row=1, column=1)

Label(choice_frame, text="Computer's Move:", font=('Arial', 14), bg='#f0f0f0').grid(row=0, column=2, padx=20)
Label(choice_frame, textvariable=computer_choice_var, font=('Arial', 24, 'bold'), fg='red', bg='#f0f0f0').grid(row=1, column=2, padx=20)

Label(root, textvariable=result_var, font=('Arial', 16, 'italic'), bg='#f0f0f0').pack(pady=15)

button_frame = Frame(root, bg='#f0f0f0')
button_frame.pack(pady=10)

Button(button_frame, text="Rock", command=lambda: play_game("Rock"), font=('Arial', 12), width=8, bg='#AEC6CF').grid(row=0, column=0, padx=5)

Button(button_frame, text="Paper", command=lambda: play_game("Paper"), font=('Arial', 12), width=8, bg='#AEC6CF').grid(row=0, column=1, padx=5)

Button(button_frame, text="Scissors", command=lambda: play_game("Scissors"), font=('Arial', 12), width=8, bg='#AEC6CF').grid(row=0, column=2, padx=5)