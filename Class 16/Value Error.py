# Exception

try :
    n = int(input("enter a number : "))
    print("the given number is ",n)
except ValueError as ex:
    print("An error occured :",ex)    