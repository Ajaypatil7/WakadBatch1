class Emp:
    cname="pyspiders"
    regID="py123"
    MB="Bangalore"
    def __init__(self, name, age, sal, phno):
        self.name = name
        self.age = age
        self.sal = sal
        self.phno = phno

Raju=Emp("Raju",23, 20000, 9898989898)

Raani=Emp("Raani", 25, 30000,7878787878)

print(Emp.cname,Emp.regID,Emp.MB)
print(Raju.cname,Raju.regID,Raju.MB,Raju.name,Raju.age,Raju.sal,Raju.phno)
print(Raani.cname,Raani.regID,Raani.MB,Raani.name,Raani.age,Raani.sal,Raani.phno)