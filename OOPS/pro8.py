class Bank:
    bname="ICICI"
    MBL="Mumbai"
    LROI=14
    def __init__(self, name, address, aadhar, bal):
        self.name=name
        self.address=address
        self.aadhar=aadhar
        self.bal=bal
    def display(self):
        print(""" name is {0}
        address is {1}
        aadhar no is {2}
        bal is {3}""".format(self.name, self.address, self.aadhar,self.bal))
    def withdraw(self):
        amt=int(input("Enter the amount"))
        if amt>self.bal:
            print("Enter proper amount.{0} Take Tablets and come back".format(self.name))
        else:
            self.bal-=amt4
            print("Take ur money")
            print("New bal is ", self.bal)

Mufeed=Bank("Mufeed", "Malegaon", 123456789876,50000)
Mufeed.display()
Mufeed.withdraw()