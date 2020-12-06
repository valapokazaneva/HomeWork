def multiply(*args):
    if len(args)==0:
        return
    else:
        rez=1
        for i in args:
            if type(i)!=int and type(i)!=float:
                raise ValueError
            rez*=i
    return rez   