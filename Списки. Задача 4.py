s1=input()
s2=input()
output=input("������� lengths ��� order ")
lst=[s1, s2, len(s1), len(s2), s1>s2]
if output=='lengths':
    print (f'����� �����: {lst[2]} � {lst[3]}')
elif output=='order':
    ret_var="�����" if lst[-1] else "��"
    print (f'������ {s1} ���� {ret_var} ������ {s2} ')