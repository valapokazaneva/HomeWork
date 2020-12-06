l1=list('abcd')
d1={'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10}
rez=0
for i in l1:
    if i in d1:
        rez=rez+1
print (rez)