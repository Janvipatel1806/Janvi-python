d={1:"Janvi",2:"Nirja",3:"Manali",4:"Neha",5:"Janki"}
print(d)
print(d.get(3))  #it returns a value of key
print(d.items()) #it returns all values and their key
print(d.keys())  #returns a key
print(d.values()) #returns a values of their keys
d.pop(5)    #pop the item at spacific index
print(d)
d.popitem() #delete a last item
print(d)
d1={101:"AAA",102:"BBB"}
d.update(d1)  #it is used as a extends in a dictonary
print(d)
print("******************************")
for i in d:
   print(i," ",d[i])
   


