# Weather Prediction

weather = (1,0,0,1,1,0,1,0,0)

s = 0
r = 0
for i in weather:
    if i == 0:
        s+=1
    else:
        r+=1

if s > r:
    print("The weather is good") 
else:
    print("the weather is not good")               