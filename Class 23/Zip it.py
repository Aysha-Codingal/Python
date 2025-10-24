# Zip it

s1 = ('s1','s2','s3')
s2 = (1,2,3)
s3 = list(zip(s1,s2))
print(s3)

list1  = [1,2,3,4]
list2 = [100,200,300,400]

list3 = list(zip(list1,list2[::-1]))
print(list3)

stocks = ('reliance','infosys','tcs')
prices = (2342,1234,4532)

stock_dic = {stock:price for stock,price in zip(stocks,prices)}
print(stock_dic)