class Emp:
    cname="google"
    cemail="hrgoogle@gmail.com"
    cphno= 1234567890
Vikas=Emp()
Pawan=Emp()
print("Accessing using class name")
print(Emp.cname, Emp.cemail, Emp.cphno)
print("Accessing using the object name")
print(Vikas.cname, Vikas.cemail, Vikas.cphno)
print(Pawan.cname, Pawan.cemail, Pawan.cphno)
Emp.cname="Amazon"
print("Accessing using class name")
print(Emp.cname, Emp.cemail, Emp.cphno)
print("Accessing using the object name")
print(Vikas.cname, Vikas.cemail, Vikas.cphno)
print(Pawan.cname, Pawan.cemail, Pawan.cphno)