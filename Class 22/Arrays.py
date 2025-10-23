# Arrays

import array as arr

a = arr.array("i",[223,55,67,78,344,73,78,78])
print("The array elements ",a)

print("The no of elements 78 is ",a.count(78))

a.reverse()
print("The reverse of the array is ")
print(a)