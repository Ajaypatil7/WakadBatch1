def store(name, p,q):
    name.m=p
    name.n=q

class A:
    x=10
    y=20

obj1=A()
store(obj1, 30,40)

obj2=A()
store(obj2, 50,60)
print("States of A", A.x, A.y)
print("States of Obj1", obj1.x, obj1.y,obj1.m, obj1.n)
print("States of Obj2", obj2.x, obj2.y,obj2.m, obj2.n)