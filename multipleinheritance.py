class A:
    def getA(self,a):
        self.a=a
        return self.a
class B:
    def getB(self,b):
        self.b=b
        return self.b
class C(A,B):
    def getc(self,c):
        self.c=c
        return self.c
    def sum(self):
        return(self.a+self.b+self.c)
c1=C()
print(c1.getA(int(input("Enter value A="))))
print(c1.getB(int(input("Enter value B="))))
print(c1.getc(int(input("Enter value c="))))
print("Sum is ",c1.sum())
