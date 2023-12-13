def Quarter(x:float,y:float)->str:
    '''Возвращает номер четверти в которой находится точка с координатами х у'''
    if x > 0 and y > 0: return f'Точка с координатами {x,y} находится в первой четверти'
    if x < 0 and y > 0: return f'Точка с координатами {x,y} находится во второй четверти'
    if x < 0 and y < 0: return f'Точка с координатами {x,y} находится в третьей четверти'
    if x > 0 and y < 0: return f'Точка с координатами {x,y} находится в четвёртой четверти'

#main

flag = 0
while flag < 3:
    try:
        x = float(input('Введите ненулевую координату х: '))
        if x==0: print('Вы ввели нулевую координату(((')
        else:
            y= float(input('Введите ненулевую координату y: '))
            if y == 0: print('Вы ввели нулевую координату(((')
            else: 
                print(Quarter(x,y))
                flag+=1
    except ValueError:
        print('Вы ввели не число')


# flag = 0
# while flag < 3:
#     try:
#         x = float(input('Введите ненулевую координату х: '))
#         y= float(input('Введите ненулевую координату y: '))
#         if x!=0 and y!=0: 
#             print(Quarter(x,y))
#             flag+=1
#         else:    
#             print('Зачем вы ввели нулевую координату?(')
#     except ValueError:
#         print('Вы ввели не число')

