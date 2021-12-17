class A:
    a = 10
    b = 20
    def __init__(self, c, d):
        self.c = c
        self.d = d
    def display(self):
        print(self.c, self.d)
    def modifyC(self, c):
        self.c = c
    @classmethod
    def display_class(cls):
        print(cls.a, cls.b)
    @classmethod
    def modifyB(cls, b):
        cls.b = b
oa = A(1, 2)
ob = A(3, 4)
oa.display()
ob.display()
A.display_class()  # using class name
oa.display_class()  # using object name