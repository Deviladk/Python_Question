class Student:
    coll="HIT"
    def __init__(self,name,dept,roll):
        self.name=name
        self.dept=dept
        self.roll=roll

    def Show(self):
        print("Name =",self.name,"\nDept =",self.dept,"\nRoll no. =",self.roll,"\nCollege =",self.coll)

stu1=Student("Aditya kiran","IT",19)
stu1.Show()