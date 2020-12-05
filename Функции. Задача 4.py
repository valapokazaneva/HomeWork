def multiply(*args):
    if len(args)==0:
        return
    else:
        rez=1
        for i in args:
            rez*=i
    return rez    