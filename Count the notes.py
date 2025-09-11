# Denomination calculator

amt = int(input("enter the amount  :  "))

note100 = amt // 100
note50 = (amt%100)// 50
note10 = ((amt%100)%50)//10

print("the 100 rs note : ",note100)
print("the 50 rs note : ",note50)
print("the 10 rs note : ",note10)
