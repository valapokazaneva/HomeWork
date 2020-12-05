a=-1001
b=100
lst=[]
for number in range(a, b+1):
    if number<=1:
        continue
    for i in range(2, number//2+1):
        if number%i==0:
            break
    else:
        lst.append(number)
print(lst)