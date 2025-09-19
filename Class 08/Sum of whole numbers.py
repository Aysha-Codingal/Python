# Sum of whole numbers

n = int(input("enter the number : "))

sum = 0 

for i in range(0,n+1):

  sum += i

print(f"The sum of number from 0 to {n} is {sum}")