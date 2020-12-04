a=input('Введите строку ')
s=list(a)
print ("Список из всех симоволов:",s)

k=a.split()
print("Список из всех слов:",k)

m=[]
for i in a:
    if i.isdigit():
        m.append(i)
print("Список из всех цифр:",m)