class FirstClass:
    __a = 2
    def _init_(self):
        self.name =''' narayana'''
        self.alpha = 'a'
        self.pi = 3.14

    def getname(self):
        return self.name

class SecondClass(FirstClass):
    def setname(self,name):
        self.name = name
        self.getname()


s =  SecondClass()
s.setname("Sitara")
print(s.getname())




