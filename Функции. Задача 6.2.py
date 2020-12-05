def calc_op(s, oper_d):
    s=s.split()
    if len(s)!=3:
        raise IndexError(f'В строке {len(s)} аргумента(ов) вместо 3')
    return oper_d[s[1]](int(s[0]), int(s[2]))