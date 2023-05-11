class A:
    def show(self):
        print("This is a show method of A class")
class B(A):
    def show(self):
        super().show()
        print("This is a show method of B class")
class c(A):
    def show(self):
        super().show()
        print("This is a show  method of c class")
class D(B,c):
    def show(self):
        super().show()
        print("This is a show method of D class")
d1=D()
d1.show()
