def RootK(X:float,K:int,N:int)->float:
    if N == 0: return 1
    Y = RootK(X,K,N-1)
    return Y - (Y - X/(Y**(K-1)))/K

# main

try:
    X = float(input('Введите положительное вещественное число X(>1): '))
    if X<1: 
        print('Число должно быть положительным')
        exit(0)
except ValueError:
    print('Вы что-то не то ввели')
    exit(0)

try:
    K = int(input('Введите целое число извлекаемой степени(>1): '))
    if K<2: 
        print('Число извлекаемой степени должно быть больше 1')
        exit(0)
except ValueError:
    print('Вы что-то не то ввели')
    exit(0)

flag = 0
while flag<6:
    try:
        N = int(input('Введите целое положительное число(?класс точности?): '))
        if N>0:
            try:
                print(RootK(X,K,N))
                flag+=1
            except RecursionError: 
                pass
                print("Чуть меньше, пожалуйста")
        else:
            print('Число должно быть положительным')
    except ValueError: 
        print('Вы не ввели целое цисло')




