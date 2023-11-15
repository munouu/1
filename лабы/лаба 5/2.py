
while True:
    while True:
        try:
            a = float(input('Введите длину отрезка A: '))
            if a<0: print('\n',"Длина отрезка должна быть положительной",'\n')
            else: break
        except ValueError: print('\n',"Введите корректное значение",'\n')
    while True:
        try:
            b = float(input('Введите длину отрезка B: '))
            if a<=b: print('\n',"Длина отрезка B должна быть меньше А",'\n')
            elif b<0: print('\n',"Длина отрезка должна быть положительной",'\n')
            else: break
        except ValueError: print("Введите корректное значение")
    counter = 0
    while a>0:
        if (a-b)>=0: a-=b; counter+=1  
        else: break
    print('\n','Длина незанятой части отрезка A =',a,'\n','Вместилось -',counter,'отреза(ов) В','\n')

