def mult(x, y=1, z=1):
    return x*y*z
a1=(15, 10, 5)
a2=(3, 1)
a3=[2, 35, 55]
a4=(5, 10, 15, 20)
print(mult(*a1))
print(mult(*a2))
print(mult(*a3))
print(mult(*a4[:3]))
print(mult(*a4[-3:]))