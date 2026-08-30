from colorama import Fore, Style
import random

ch = ["rock", "paper", "scissors"]
while True:
    comp = random.choice(ch)
    user = input(Fore.BLUE + "enter Rock or Paper or Scissors : " + Style.RESET_ALL)
    print(comp)
    if comp.lower() == user.lower():
        print(Fore.YELLOW + "TIE !!! 🔗" + Style.RESET_ALL)
    elif (user.lower() == 'rock' and comp.lower() == 'scissors') or (user.lower() == 'paper' and comp.lower() == 'rock') or (user.lower() == 'scissors' and comp.lower() == 'paper'):
        print(Fore.GREEN + "You win the game 🏆" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Computer Win 😒" + Style.RESET_ALL)
    choice = input(Fore.BLUE + "Do you want to play again (y/n) : " + Style.RESET_ALL)
    if choice.lower() == "n":
        break