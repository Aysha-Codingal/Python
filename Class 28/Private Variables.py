# private variables
class myclass:
    __priv_var = 12
    def __priv_meth(self):
        print("this is a private method")

    def pub_meth(self):
        print("the value is", self.__priv_var)
m1 = myclass()
m1.pub_meth()
m1.__priv_var = 34
m1.__priv_meth()
   