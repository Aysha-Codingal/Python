# Armstrong Number

n = int(input("enter the number : "))

temp = n
sum = 0
while temp > 0:
    rem = temp%10
    sum = sum + rem**3
    temp = temp//10

if n == sum:
        print(n,"in a armstrong number")
else:
        print(n,"in a not armstrong number")