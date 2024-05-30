  # Tuple problem

#creat tuple
obj =(1,2,3,4,"hi")
#chek type
print(type(obj))
#check length
print(len(obj))

#access tuple element
print(obj[0])
print(obj[1])
print(obj[2])
print(obj[3])
print(obj[4])

# or
print(obj)

# or
for ele in obj:
    print(ele)

#slice
#creat new tuple because you cant change in tuple
obj1=obj[2:4]
print(obj1)

print(type(obj1))
print(len(obj1))
