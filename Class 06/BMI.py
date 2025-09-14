# BMI calculator

w = float(input("enter your weight in kg : "))
h = float(input("enter your weight in m : "))

bmi = w/(h ** 2)

if bmi < 18.5:
    print("your bmi is ",bmi)
    print("you are under weight")
elif bmi < 24.5:
    print("your bmi is ",bmi)
    print("you are healthy")
elif bmi < 30:
    print("your bmi is ",bmi)
    print("you are over weight")
else:
    print("your bmi is ",bmi)
    print("you are Obese")
 
