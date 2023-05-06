s=input("Enter string")

a=s.split()
d={}
c=1

for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=c
        
print(d)

        
