s1=input()
s2=input()
output=input("Введите lengths или order ")
lst=[s1, s2, len(s1), len(s2), s1>s2]
if output=='lengths':
    print (f'Длины строк: {lst[2]} и {lst[3]}')
elif output=='order':
    ret_var="ПОСЛЕ" if lst[-1] else "ДО"
    print (f'Строка {s1} идет {ret_var} строки {s2} ')