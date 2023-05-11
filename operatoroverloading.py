class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(x,y)
        print("Hello")
    def __str__(self):
        print("str method called")
        return"[{0},{1}]".format(self.x,self.y)
    def __add__(self,obj):
        print("add method called")
        p=self.x+obj.x
        q=self.y+obj.y
        return A(p,q)
a1=A(10,20)
print(a1)
a2=A(30,40)
print(a2)
print("Addition of 2 objects ",a1+a2)
