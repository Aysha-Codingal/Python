# Check the frequency

list1 = { "codingal" : 2, "is" : 2, "coding":3, "python":2,"primary":2} 
count = 0
k = 2
for key in list1.values():
    if key == k:
            count +=1
print(f"The total number of words which has frequecy {k} is {count} ")            