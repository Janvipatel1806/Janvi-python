class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("Value of A is ",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("Value of B is",self.b)
    def sum(self):
        print("Sum is",self.a+self.b)
b=B()
b.getA(int(input("Enter the value of A")))
b.putA()
b.getB(int(input("Enter the value of B")))
b.putB()
b.sum()

