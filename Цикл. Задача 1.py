a='asdfghjkfghjkll'
b='fghjfghjkkl'
c=''
for i in a:
    if i in b and i not in c:
        c+=i
print(c)