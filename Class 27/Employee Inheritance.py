# Employee Inheritance
class person:
    def __init__(self,id,name):
        self.id =id
        self.name = name
    def display(self):
        print("My id is",self.id)    
        print("My name is ",self.name)

class employee(person):
    def __init__(self,salary,post,id,name):
        self.salary = salary
        self.post = post
        person.__init__(self,id,name)
    def display1(self):
        self.display()    
        print("My salalry is ",self.salary)
        print("I am an ",self.post)


e1 = employee(50000,"Engineer","102","Mathew")        
e1.display1()
             
        
