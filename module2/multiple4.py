n=input("enter a string=")
a=len(n)
if(a%4==0):
    print(n[::-1])
else:
    print("string is not a multiple of four so we cannot revrce it")
