class Shape:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    def area(self):
        return self.len*self.wid
    
obj1=Shape(5,4)
print("Area of obj1 is :",obj1.area())