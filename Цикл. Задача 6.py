#��� ������������ ������ ������� �� �������, ������ ������� � ������ (�� �������!) ����� ����� ������ ��� �������. ��� ������ "Hello world!" ������ ���������� "Hell !".

stroka=str(input("������� ������ "))
d=len(stroka)
print("����� ������ �����", d)
simvol=""
for i in range(d):
    if d%(i+1)==0:
        simvol+=stroka[i]
print(simvol)