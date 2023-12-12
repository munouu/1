def InvertDigits(k):
    return k[::-1]

#main

flag = 0
k = 0
while flag<5:
    try:
        k = int(input('Введите целое положительное число: '))
        if k>0:
            k = str(k)
            print(InvertDigits(k))
            flag+=1
        else:
            print('Число должно быть положительным')
    except ValueError: 
        print('Вы ввели не число')
        
        



