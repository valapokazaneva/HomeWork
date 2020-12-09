a=[18, 2, 8, 3, 55, 2]
minimum=a[0]
min_index=0
second_min=a[0]
second_min_ind=0
for ind, element in enumerate(a):
    if element<minimum:
        minimum=element
        min_index=ind
if a.count(minimum)==2:
    print(minimum)
    print(min_index)
else:
    for ind, element in enumerate(a):
        if element>minimum and element<second_min:
            second_min=element
            second_min_ind=ind
    print(second_min)
    print(second_min_ind)