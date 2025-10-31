# Employee in and Out
class employee:
    def __init__(self):
        print("The object is created")
    def __del__(self):
        print("The object is deleted ")        

e1 = employee()        

print("I'm in the main program")
del e1