# Factorial (Recursion)

def recurse(x):
    if x == 1:
        return 1
    else:
        return x * recurse(x-1)

print("The factorial of 3 is ",recurse(3))        
