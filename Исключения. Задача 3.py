def calc(s):
    calc_dict={
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x/y,
        '%': lambda x, y: x%y,
        '^': lambda x, y: x**y,
    }
    s=s.split()
    assert len(s)==3, "����������� ������� ���������"
    assert s[0].isdigit(), "������ ���� �� �������� ������"
    assert s[-1].isdigit(), "��������� ���� �� �������� ������"
    assert s[1] in calc_dict, "������ �������� �� ��������������"
    
    try:
        return calc_dict[s[1]](int(s[0]), int(s[-1]))
    except ZeroDivisionError:
        print("������� �� ����")