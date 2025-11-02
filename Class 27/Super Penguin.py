# Super Penguin

class bird:
    def __init__(self):
        print("The bird is ready")

    def wings(self):
        print("I have wings and feathers")    

class penguin(bird):
    def __init__(self):
        print("The penguin is ready")
        super().__init__()

    def run(self):
        print("I can run faster")        

p1 = penguin()        
p1.wings()
p1.run()
       
