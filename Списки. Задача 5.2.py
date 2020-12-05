max_val=10 
repeat=int(input("¬ведите целое положительное число ")) 
b=[]
lst=list(range(1, max_val+1))*repeat
print(lst)
a=lst[len(lst)//4:len(lst)*3//4+1]
print(a)
for i in a:
    i=i*10
    b.append(i)
print(b)