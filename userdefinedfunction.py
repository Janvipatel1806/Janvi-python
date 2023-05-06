#Function with no argument and no return value.
def stu():
    print("Hello,Good morning")
stu()
#Function with argument but no return value.
def add(a,b):
    c=a+b
    print(c)

a=int(input("Enter number 1="))
b=int(input("Enter number 2="))
add(a,b)

#Function with no argument but return a value
def add():
    a=int(input("Enter number 1="))
    b=int(input("Enter number 2="))
    c=a+b
    return(c)
x=add()
print(x)
#Function with argument and return a value
def add(a,b):
   c=a+b
   return(c)
q=add(10,20)
print(q)
    
