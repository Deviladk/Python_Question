class Body:
    def fun1(self):
        print("I am body")
class Engine:
    def fun2(self):
        print("I am engine")
class Car(Body,Engine):
    def fun3(self):
        print("I am car")

Tata=Car()
Tata.fun1()
Tata.fun2()
Tata.fun3()