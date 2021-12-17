class Student:
    C_name="DYPATIL"
    reg_no=123
    address= "Talegaon"
    def __init__(self,name, roll_no, phno, email):
        self.name=name
        self.roll_no=roll_no
        self.phno=phno
        self.email=email
    def display(self):
        print("College name is", self.C_name)
        print("reg_no is", self.reg_no)
        print("Address is", self.address)
        print("name is ", self.name)
        print("roll_no is", self.roll_no)
        print("phno is {0} and email is{1}".format(self.phno,self.email))
    def modify_phno(self, new):
        self.phno=new

Pawan=Student( 'Pawan', 420, 9898989898, "BewafaPawan@gmail.com" )
Ashwin=Student( "Ashwini",426,7878787878,"AngelAshwini@gmail.com")

print(Student.C_name, Student.reg_no,Student.address)
Student.display(Pawan)   #cALLING THE OBJECT METHOD USING CLASS NAME
Ashwin.display()  #CALLING THE OBJECT METHOD USING OBJECT NAME
print("********************************************")
Pawan.modify_phno(888888888888)
Student.modify_phno(Ashwin, 66666666666)
Pawan.display()
Ashwin.display()