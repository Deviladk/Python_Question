from abc import ABC,abstractmethod

class Car(ABC):
    def fun1(self):
         print("I have 4 wheel")
    
    @abstractmethod
    def fun2(self):
        pass

class Tata(Car):
    def fun2(self):
        print("Tata key")
        self.fun1()

class Nano(Car):
    def fun2(self):
        print("Nano key")
        self.fun1()

obj1=Tata()
obj2=Nano()
obj1.fun2()
obj2.fun2()


        