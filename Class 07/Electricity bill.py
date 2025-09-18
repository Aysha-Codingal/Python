# Electricity bill

u = int(input("enter the units consumed : "))

if u < 50:
    amt = u * 2.45 + 25
elif u < 100:
    amt = u * 3.25 + 35
elif u < 200:
    amt = u * 5.26 + 45
else:
    amt = u * 8.45 + 75
    
print("The electricity amt is ",amt)    
