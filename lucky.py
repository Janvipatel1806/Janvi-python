import random
l=[]
lucky=[]
for i in range(1,101):
    l.append(i)
for i in range(11):
    lucky.append(random.choice(l))
    l.remove(lucky[i])
print(l)
print(lucky)