class Car:
    def fun1(self):
        print("start,break,stop")
class Tata(Car):
    def fun2(self):
        print("Tata key")


car1=Tata()
car1.fun1()
car1.fun2()