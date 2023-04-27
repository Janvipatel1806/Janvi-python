n=input("Enter a string ")
space=0
digit=0
alpha=0
spch=0
for i in n:
    if(i.isalpha()):
        alpha+=1
    elif(i.isdigit()):
        digit+=1
    elif(i.isspace()):
        space+=1
    else:
        spch+=1
print("Total Alphabet",alpha)
print("Total space",space)
print("Total digit",digit)
print("Total special charater",spch)

