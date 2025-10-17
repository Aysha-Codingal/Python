# Tuple Operations

# mixed tuple

my_tuple = (12,45,66,99,'cat')
print(my_tuple)

int_tuple = (12,34,45,56,64,22)
print(int_tuple)

int_tuple = int_tuple + (1000,)
print(int_tuple)

# Count
print (int_tuple.count(45))
print(int_tuple[3:6])
print(int_tuple[:6])