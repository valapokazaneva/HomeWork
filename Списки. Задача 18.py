lsls=[[1,2,3],['a', 'b'], [30, 40, 50, 60]]
lst1=[]
lst2=[]
min_len=len(lsls[0])
for i in lsls:
    if len(i)<min_len:
        min_len=len(i)
for i in range(min_len):
    for j in lsls:
        lst1.append(j.pop(0))
print(lsls)
for i in lsls:
    lst2.extend(i)
print(lst1, lst2)