bag=[]
while True:
    inp=input()
    if inp=='':
        print(bag)
        break
    elif inp in bag:
        print("����� �������� ��� ���� � �����")
        continue
    else:
        if len(bag)==5:
            print(f'��������� ��������: {bag.pop(0)}')
            bag.append(inp)
            print(f'����������� ��������: {bag[-1]}')
        else:
            bag.append(inp)
            print(f'����������� ��������: {bag[-1]}')