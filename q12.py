class Student:
    c=0
    def __init__(self,name):
        self.name=name
        Student.c+=1 

    @staticmethod
    def count():
        print("Total number of student is :",Student.c)   

obj1=Student("Aditya")
obj2=Student("Kiran")
obj2.count()
