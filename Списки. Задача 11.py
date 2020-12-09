lst=[3, 6, 7, 12]
lst1=[]
for i in lst:
    condition=True
    number=i
    lst_simple=[]
    while condition:
        for j in range(2, number+1):
            for k in range(2, j//2):
                if j%k==0:
                    break
            else:
                if number%j==0:
                    lst_simple.append(j)
                    number=number//j
                    break
        if number==1:
            condition=False
    lst1.extend(lst_simple)
print(lst1)