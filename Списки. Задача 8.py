s1="один два три"
s2="альфа бетта гамма"
s1=s1.split()
s2=s2.split()
l=len(s1) if len(s1)<len(s2) else len(s2)
lst=[]
for i in range(l):
    lst.append(s1[i])
    lst.append(s2[i])
lst=' '.join(lst)
print(lst)