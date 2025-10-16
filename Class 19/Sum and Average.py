# Sum and Average

a = [78,89,98,99,89,23]
sum = 0
for i in a:
    sum += i

avg = sum/ len(a)
print("the sum of the list is ",sum)    
print("the average of the list is ",round(avg,2))    

print("the largest element in the list is ",max(a))
print("the smallest element in the list is ",min(a))