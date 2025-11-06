# class computer
class computer:
    def __init__(self):
        self.__maxprice = 900
    
    def setprice(self, price):
        self.__maxprice = price
        
    def printprice(self):
        print("the price is", self.__maxprice)

c1 = computer()        
c1.printprice()

c1.__maxprice = 100
c1.printprice()

c1.setprice(1200)
c1.printprice()