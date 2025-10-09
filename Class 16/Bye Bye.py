# BYE BYE

try:
    valid = False
    while not valid:
        n = int(input("enter a number : "))
        while n % 2 == 0:
            print("bye")
        print(n)
        valid = True
except ValueError as ex:
    print("The value error occured : ",ex)        