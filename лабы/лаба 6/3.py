from numpy import * 

try:
    lenght = int(input("Введите длину списка: "))
    
except ValueError: 
    print("ЦИФР ЗНАЕШ КТО ТАКОЙ?")
    exit(0)

hi = 20
lo = -5

sp = list(random.randint(lo, hi, lenght))
print('\n','Ваш список: ',*sp)

sumpos = 0
flag = 0
divFour_sp = []

for el in range(0,len(sp)):

    if sp[el]>=0 and flag == 0:
        sumpos+=sp[el]
    else: 
        flag+=1
    
    if sp[el]%4==0 and sp[el]!=0:
        divFour_sp+=[sp[el]**2]

print('\n',f'Сумма элементов списка, расположенных до первого отрицательного: {sumpos} \n \
Квадраты элементов, картных 4: {divFour_sp} \n \
Колличество элементов, кратных 4: {len(divFour_sp)}\n')

    

    