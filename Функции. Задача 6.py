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
    return calc_dict[s[1]](int(s[0]), int(s[-1]))