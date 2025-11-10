from abc import ABC,abstractmethod
class abstact_class(ABC):
    def print_x(self,x):

        print("the value of x is",x)

    @abstractmethod
    def task(self):
        pass


class sub_class(abstact_class):
    def task(self):
        print("I am inside abstract class")


obj1 = sub_class()    
obj1.print_x(100)
obj1.task()

