# Pair of Elements

class paiofelements:
    def twosum(self,tuple1,target):
        lookup = {}
        sum = 0
        for i,value in enumerate(tuple1):
            sum = sum + value
            lookup[i] = sum
            if sum >= target :
                print("The position is",i)
                print(lookup)
                return
            print(lookup)
            print("The target is not reached")
p1 = paiofelements()
tuple1 = (10,20,30,40,50,60,70,80,90)
target = 100
p1.twosum(tuple1,target)
             