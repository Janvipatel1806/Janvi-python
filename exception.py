try:
    a=int(input("Enter number 1="))
    b=int(input("Enter number 2="))
    c=a/b
    print(c)
except Exception as e:
    print("Exception" ,e)
finally:
    print("Hello")
    

