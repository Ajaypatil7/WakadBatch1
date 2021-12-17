class A:
    x=10
    y=20
obj1=A()
obj2=A()
print("Accessing The class data using class name")
print(A.x, A.y)
print("Accessing the class data using object name")
print(obj1.x, obj1.y)
print(obj2.x, obj2.y)
print("Modifying the class data using class name")
A.x=77
print("Accessing The class data using class name After Modification")
print(A.x, A.y)
print("Accessing the class data using object name After Modification")
print(obj1.x, obj1.y)
print(obj2.x, obj2.y)
