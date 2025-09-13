# Profit loss

cp = float(input("enter the cost price of the product : "))
sp = float(input("enter the selling price of the product : "))

if cp<sp:
    print(f"you got a profit of ${sp-cp}")
    
else:
   print(f"you got a loss of ${cp-sp}")

