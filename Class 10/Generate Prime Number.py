# Generate a Prime Number

l = int(input("Enter the lower limit: "))
u = int(input("Enter the upper limit: "))

print("the prime numbers are : ")
for i in range(l,u+1):
    for j in range (2,i):
        if i%j == 0:
            break
    else:
        print(i) 
