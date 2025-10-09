# Multiple exceptions

try:
    n1,n2 = eval(input("Enter the n1, n2 seperate by commas : "))
    d = n1/n2
    print(d)
except SyntaxError as ex:
    print(" The exception error as : ",ex) 
except ZeroDivisionError as ex:
    print(" The erro is : ",ex) 
except:
    print("Error occured") 
finally : 
    print("What ever happens i will be there")    

