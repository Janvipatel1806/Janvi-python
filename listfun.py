l= [1,2,"janvi",3,4,5,"Nirja",4]
print(l)   #print the list
l.append(899)   #insert at the last
print(l)
l1=l.copy()   #copy the list into another  list 
print(l1)
l1.append(23)
print(l1)
print(l)
print(l.count(4))   #count the number of value in list
l2=[1,2,3,4,5,6,7,8]
l.extend(l2)
print(l)
l1=l2       #copy
print(l1)
print(l.index(2))   #display the index 
l.insert(4,"yash")  #insert a record at spacific position
print(l)
l.pop()     #delete a last element
print(l)
l.pop(2)    #pop the the element at spacific index
l.remove("yash")    #remove a spacific element
print(l)
l1.reverse()    #reverse a list 
print(l1)
l.clear()
print(l)





