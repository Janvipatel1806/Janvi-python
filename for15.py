for i in range(1,6):
    if(i%2!=0):
        print(" "*(6-i)," *"*(i))
    else:
        print(" "*(6-i)," -"*(i))
for j in range(2,6):
    if(j%2!=0):
        print(" "*j," *"*(6-j))
    else:
        print(" "*j," -"*(6-j))
