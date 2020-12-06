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
    assert len(s)==3, "Некорректно введено выражение"
    assert s[0].isdigit(), "Первый знак не является числом"
    assert s[-1].isdigit(), "Последний знак не является числом"
    assert s[1] in calc_dict, "Данная операция не поддерживается"
    
    try:
        return calc_dict[s[1]](int(s[0]), int(s[-1]))
    except ZeroDivisionError:
        print("Деление на ноль")