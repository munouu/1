from numpy import * 

try:
    lenght = int(input("Введите длину списка: "))
    if lenght<=0: 
        print('Длина списка не может быть отрирцательна или равна 0')
        exit(0)
    
except ValueError: 
    print("ЦИФР ЗНАЕШ КТО ТАКОЙ?")
    exit(0)

hi = 20
lo = -5

sp = list(random.randint(lo, hi, lenght))
sp+=[]
print('\n','Ваш список: ',*sp)

sumpos = 0
divFour_sp = []
flag = 0

for el in range(len(sp),0,-1):

    if sp[el-1]>0: 
        flag+=1 #флаг перестаёт быть нулём при первом появлении положительного с конца

    if flag>0: #
        sumpos+=sp[el-1]

    if sp[el-1]%4==0 and sp[el-1]!=0:
        divFour_sp+=[sp[el-1]**2]

print('\n',f'Сумма элементов списка, расположенных до последнего положительного: {sumpos} \n \
Квадраты элементов, картных 4: {divFour_sp} \n \
Колличество элементов, кратных 4: {len(divFour_sp)}\n')

    

    