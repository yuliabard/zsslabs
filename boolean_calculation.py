print("Ноль в качестве знака операции завершает работу программы")
while True:
    s=input('Введите логическую операцию (or,and,not,xor):')
    if s=='0': break
    if s in ('or','and','not','xor'):
        print('Введите x, y, равные 0 или 1:')
        x=float(input('x ='))
        y=float(input('y ='))
        if s=='or':
            print('x v y =',(x or y))
        elif s=='and':
            print('x & y =',(x and y))
        elif s=='not':
            print('x = ',not(x))
            print('y = ',not (y))
        elif s=='xor':
            print('x + y =',((x and not y) or (not x and y)))
    else:
        print('Неверный знак операции')