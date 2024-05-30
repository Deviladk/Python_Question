def add(num1=None,num2=None,num3=None):
    sum=0
    if num1==None:
        return sum
    elif num2==None:
        sum=num1
    elif num3==None:
        sum=num1+num2
    else:
        sum = num1+num2+num3

    return sum

print(add())
print(add(5))
print(add(5,6))
print(add(5,6,7))