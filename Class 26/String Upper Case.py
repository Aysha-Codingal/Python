# String Upper Case
class IOString:
    def __init__(self):
        self.srt1 = ""
    def getstring(self):
        self.str1= input("entr a phrase : ") 
    def upperstr(self):
        print("The upper case of the given string is ",self.str1.upper())        

obj1 =  IOString()    
obj1.getstring()    
obj1.upperstr()


