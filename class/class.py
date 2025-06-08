class myClass:
    def __init__(self,name, sal):
        self.Name = name
        self.Sal = sal
    def f(self):
        print(self.Name)
        return 'Gouri'

mc = myClass("House",34567)
mc.f()

class chi(myClass):
    pass

ch = chi("House2", 932234)
ch.f()