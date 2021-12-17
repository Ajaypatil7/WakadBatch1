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
        print("Bank name is ", self.bname)
        print("MBL is ", self.MBL)
        print("LROI is", self.LROI)
        print(""" 
        name is {0}
        address is {1}
        aadhar no is {2}
        bal is {3}""".format(self.name, self.address, self.aadhar,self.bal))
    @classmethod
    def modify_bname(cls, new):
        cls.bname=new

Mufeed=Bank("Mufeed", "Malegaon", 123456789876,50000)
Pawan=Bank("Pawan", "Buldhana", 123456789789, 30000)
Bank.display(Mufeed)
Pawan.display()
#BAnk.bname="ICICIBANK"
Bank.modify_bname("ICICIBANK")
print("**************************************")
Bank.display(Mufeed)
Pawan.display()
