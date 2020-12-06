import random
ri1=[random.randint(1, 15) for _ in range(30)]
print(ri1)
ri2=[]
ri3=[]
for i in ri1:
    if i not in ri2:
        ri2.append(i)
print(ri2)
ri2=sorted(ri2)
print(ri2)