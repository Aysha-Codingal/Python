class UAE:
    def capital(self):
        print("The capital city of UAE is Abu Dhabi")

    def language(self):
        print("The widely spoken language in UAE is Arabic")        

    def type(self):
        print("UAE is a federal semi-constitutional monarchy")     

class Germany:
    def capital(self):
        print("The capital city of Germany is Berlin")

    def language(self):
        print("The widely spoken language in Germany is Hochdeutsch")        

    def type(self):
        print("Germany is a democracy country")     

obj1 = UAE()
obj2 = Germany()
for i in (obj1,obj2):
    i.capital()
    i.language()
    i.type()




