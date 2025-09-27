# Floyd’s triangle

n = int(input("enter the number of rows : "))
k = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(k, end=" ")
        k+=1
    print()