bag=[]
while True:
    inp=input()
    if inp=='':
        print(bag)
        break
    elif inp in bag:
        print("Такое значение уже есть в мешке")
        continue
    else:
        if len(bag)==5:
            print(f'Удаленное значение: {bag.pop(0)}')
            bag.append(inp)
            print(f'Добавленное значение: {bag[-1]}')
        else:
            bag.append(inp)
            print(f'Добавленное значение: {bag[-1]}')