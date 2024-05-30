class Math:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        s=self.num1+self.num2
        print("sum of two number is",s)
    
temp=Math(5,7)
temp.add()
