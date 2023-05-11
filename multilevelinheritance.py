class A:
    def getA(self,a):
        self.a=a
        return self.a
class B(A):
    def getB(self,b):
        self.b=b
        return self.b
class C(B):
    def getC(self,c):
        self.c=c
        return self.c
    def sum(self):
        return(self.a+self.b+self.c)
c1=C()
print(c1.getA(int(input("Enter value of A"))))
print(c1.getB(int(input("Enter value of B"))))
print(c1.getC(int(input("Enter value of c"))))
print("Sum is ",c1.sum())
        
