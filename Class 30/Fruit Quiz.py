# Fruite Quiz 
import random

class Fruit_Quiz:
    def __init__(self):
        self.fruits = {"Apple" : "red",
                       "Banana" : "yellow",
                       "Orange" : "orange",
                       "Watermelon" : "red "}

    def quiz(self):
        while True:
            fruit,color = random.choice(list(self.fruits.items()))
            print("WHAT IS THE COLOR OF ",fruit) 
            user = input()                      
            if color == user:
                print("CONGRATULATIONS !!!") 
            else:
                print("PLEASE TRY AGAIN")    
            ch = input("DO YOU WANT TO CONTINUE ? Y / N : ")   
            if ch.lower() == 'n':
                break
f1 = Fruit_Quiz()
f1.quiz()
