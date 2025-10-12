# Rock paper scissors

import random

list1 = ['rock','paper','scissors']

while True :
    comp = random.choice(list1)
    user = input("enter rock or paper or scissors :")
    if user.lower() == comp:
        print("It is a tie!")
    elif (user == 'rock' and comp == 'scissors') or (user == 'paper' and comp == 'rock') or (user == 'scissors' or comp == 'paper'):
        print("You win !!!🏆")
        print(comp)
    else :
        print("computer win!✨")
    choice = input("do you want ot play again y/n : ")
    if choice.lower() == 'n':
        break;