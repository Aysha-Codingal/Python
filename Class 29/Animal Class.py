from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def move (self):
        pass

class human(animal):
    def move(self):
        print("I can walk and run")    

class snake(animal):
    def move(self):
        print("Snake move my slithering")    

class fish(animal):
    def move(self):
        print("Fish move my swimming")    

h1 = human()        
h1.move()
s1 = snake()
s1.move()
f1 = fish()
f1.move()




