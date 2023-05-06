def odd(n):
    if(n%2!=0):
        print(n ,"is a odd number")
    else:
        print(n ,"is not a odd number")



        
def even(n):
     if(n%2==0):
        print(n ,"is a even number")
     else:
        print(n,"is a not a even number")
   


        
def fec(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    print(s)
    




def febonaki(n):
    a=0
    b=1

    while(b<n):
         print(b)
        a,b=b,a+b
       
    

