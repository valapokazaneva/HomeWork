while True:
    inp=input("������� ���������: ")
    if inp=='STOP':
        print('Program interrupted by user')
        break
    elif inp<'a':
        print('Too early in the dictionary. Try again!')
    else:
        print(f'{inp:_^30}')