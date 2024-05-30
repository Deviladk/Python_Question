class A:
    def show(self):
        print("I am A")

class B(A):
    def show(self):
        print("I am B")

obj1=B()
obj1.show()
