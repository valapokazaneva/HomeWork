def find_length(p1,p2):
    d=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)
    return d
def square(p1, p2, p3):
    assert type(p1)==tuple, "Неправильный тип данных у p1"
    assert type(p2)==tuple, "Неправильный тип данных у p2"
    assert type(p3)==tuple, "Неправильный тип данных у p3"
    for i in p1:
        assert type(i)==float or type(i)==int, "Неправильный тип данных у координаты"
    for i in p2:
        assert type(i)==float or type(i)==int, "Неправильный тип данных у координаты"
    for i in p3:
        assert type(i)==float or type(i)==int, "Неправильный тип данных у координаты"
    line1=find_length(p1,p2)
    line2=find_length(p1,p3)
    line3=find_length(p2,p3)
    p=(line1+line2+line3)/2
    s=(p*(p-line1)*(p-line2)*(p-line3))**(1/2)
    return s