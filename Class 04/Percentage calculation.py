# Percentage calculation

m1 = int(input("ente the English mark  : "))
m2 = int(input("ente the Science mark  : "))
m3 = int(input("ente the Math mark  : "))
m4 = int(input("ente the Social mark  : "))

total = m1 + m2 + m3 + m4
per = (total/400) * 100

print("the total marks are :",total) 
print("the percentage is ",per)
