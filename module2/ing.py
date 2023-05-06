n=input("Enter a any string")
a=len(n)
if(a<3):
    print("We cannot change it because it has only three character")
else:
    if(n.endswith("ing")):
        s= n.replace("ing","ly")
        print(s)

    else:
        print(n+"ing")
   
    
    
    
