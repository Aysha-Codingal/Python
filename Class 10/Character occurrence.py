# Character occurrence

str1 = input("enter the phrase : ")
ch = input("enter the character : ")
count = 0
for i in str1:
    if ch == i:
        count+=1

print(f"the {ch} in {str1} is {count}")        
