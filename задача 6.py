#Для произвольной строки вывести те символы, номера которых в строке (не индексы!) делят длину строки без остатка. Для строки "Hello world!" должно выводиться "Hell !".

stroka=str(input("Введите строку "))
d=len(stroka)
print("Длина строки равна", d)
simvol=""
for i in range(d):
    if d%(i+1)==0:
        simvol+=stroka[i]
print(simvol)