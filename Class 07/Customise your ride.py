# Customise your ride

ch1 = input("1.Bike \n2.Car \n Enter your choice : ")
if ch1 == '1':
    ch2 = input("1.Scooty \n2.Yamaha \n Enter your choice : ")
    if ch2 == "1":
        print("you have selected Scooty ")
    elif ch2 == "2":
        print("you have selected Yamaha ")
    else:
        print("invalid input")
elif ch1 == '2':
    ch2 = input("1.XUV \n2.Sedan \n Enter your choice : ")
    if ch2 == "1":
        print("you have selected XUV")
    elif ch2 == "2":
        print("you have selected Sedan ")
    else:
        print("invalid input")
else:
    print("invalid input")
