import math

def Conv(s):

    try :
     return math.sqrt(s)
    except Exception as e:
       return e

num1=9
num2=-9

print(Conv(num1))
print(Conv(num2))