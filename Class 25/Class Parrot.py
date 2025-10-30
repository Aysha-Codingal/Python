# Class parrot

class parrot:
    species = "Maccaw"
    def __init__(self,name,age):
      self.name = name
      self.age = age

p1 = parrot("Jolly",2)      
p2 = parrot("Candy",3)      

print(f"the species is {p1.species} and my name is {p1.name}")
print(f"the species is {p2.species} and my name is {p2.name}")