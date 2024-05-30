def Div(num1,num2):
    try:
        return num1/num2
    except Exception as e:
        return e

num1=10
num2=5
num3=0
print(Div(num1,num2))
print(Div(num1,num3))