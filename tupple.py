t= ("Janvi",1,2,3,"Nirja",1.1,True,3,4,"Manali")
print(t)
print(t.count(1)) #count the number of values in tupple
print(t.index("Manali")) #returns an index
t1=("janvi",1,2,3,4,"Nirja",[1,2,"Janvi"],78,90)
t1[6].append(100)
print(t1)
print(list(t))
print("****List***")
for i in t:
    print(i)
