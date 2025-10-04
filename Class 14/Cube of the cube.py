# Cube of the cube

def cube(x):
    return x**3
def divisible(x):
    if x%3 == 0:
        return cube(x)
    else:
        return False
print(divisible(32))        
print("the cube of x is",divisible(45))
     