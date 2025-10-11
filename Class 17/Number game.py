# Number game

import random

comp = random.randint(1,10)

while True :
    user = int(input("enter the guess,(1-10) : "))
    if user == comp:
        print("You guessed it correct!!! Congatulations")
        break