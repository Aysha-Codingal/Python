# Vehicle Inheritance

class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    pass

bus1 = bus("12km/h",'15km/l')
print("the maxspeed of the bus is",bus1.maxspeed)
print("the mileage is ",bus1.mileage)

