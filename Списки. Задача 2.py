a=input('������� ������ ')
s=list(a)
print ("������ �� ���� ���������:",s)

k=a.split()
print("������ �� ���� ����:",k)

m=[]
for i in a:
    if i.isdigit():
        m.append(i)
print("������ �� ���� ����:",m)