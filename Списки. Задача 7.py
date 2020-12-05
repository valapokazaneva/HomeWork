from math import *
lst=[]
while True:
    inp=input()
    if inp.lower()=='stop':
        print('INTERRUPTED')
        break
    elif inp=='True':
        lst.append(True)
    elif inp=='False':
        lst.append(False)
    else:
        try:
            inp=float(inp)
            inp=ceil(inp)        
            lst.append(inp)
        except:
            lst=str(inp)
    print(lst)