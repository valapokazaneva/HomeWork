def calc_op(s, oper_d):
    s=s.split()
    if len(s)!=3:
        raise IndexError(f'� ������ {len(s)} ���������(��) ������ 3')
    return oper_d[s[1]](int(s[0]), int(s[2]))