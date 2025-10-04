# waiter tip

def cal_bill(amt,tip):
    tamt = amt + (amt *tip/100)
    print("The total amt is $",tamt)

amt = float(input("enter the bill amt : "))    
tip = float(input("enter the percentage for the tip : "))    
cal_bill(amt,tip)
