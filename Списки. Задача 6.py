string='test_Stringss'
lst=[]
for i, e in enumerate(string):
    if i==0 or i==len(string)-1:
        ret=e
    elif e.lower()=='s':
        ret=string[i-1]*2+string[i+1]
    else:
        ret=e
    lst.append(ret)
print(lst)