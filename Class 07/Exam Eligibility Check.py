# Exam Eligibility Check

mc = input("enter the student have medical cause or not (y/n) : ")
if mc.lower() == 'y':
    print("The student is allowed to write the exam")
elif mc.lower() == 'n':
    att = int(input("enter the attendance: "))
    if att > 75:
        print("The student is allowed to write the exam")
    else:
        print("The student is not allowed to write the exam")
else:
    print("invalid input")
