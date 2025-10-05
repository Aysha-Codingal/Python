# Break ( check alphabet 'A' is there or not)

str1 = input("enter a phrase : ")

for i in str1:
    if i.lower() == 'a':
        print("a is present in the phrase ",str1)
        break
else:
    print("a is not present in phrase : ",str1)    