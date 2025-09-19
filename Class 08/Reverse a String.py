# Reverse a String

strl = input("enter the string1 : ")
rev = ""

for i in strl:
    rev = i + rev


print(f"the reverse of '{strl}'is '{rev}'")