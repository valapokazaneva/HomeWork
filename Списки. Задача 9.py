s1="один два три"
s2="альфа бетта гамма"
s1=s1.split()
s2=s2.split()
lst=list(zip(s1, s2))
lst=' '.join([j for i in lst for j in i])
print(lst)