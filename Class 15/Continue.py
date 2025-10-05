# Continue (Reverse order skipping 5)
print("the number from 10 to 1 skipping 5")
for i in range(10,0,-1):
    if i == 5:
        continue
    print(i)