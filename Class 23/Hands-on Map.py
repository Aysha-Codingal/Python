# Hands-on Map

list1 = [1,2,45,67,89]
list2 = [9,8,729,8,67]

add = list(map(lambda x,y:x+y, list1,list2))

print("The addition of two lists are :",add)

my_list = [23,45,78,90]
def sqr(x):
    return x*x

square = map(sqr,my_list) 
print("the square of the list are :")
print(list(square))