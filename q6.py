class Name:
    def __init__(self,name):
        self.name=name
class Roll(Name):
    def __init__(self,roll,name):
        self.roll=roll
        super().__init__(name)
class Cla(Roll):
    def __init__(self,cla,roll,name):
        self.cla=cla
        super().__init__(roll,name)

    def show(self):
        print("Name=",self.name)
        print("class=",self.cla)
        print("Roll no.=",self.roll)

obj1=Cla("IT",19,"ADITYA KIRAN")
obj1.show()
