from random import randint

try:
    m = int(input("Введите кол-во строк: "))
    n = int(input("Введите кол-во столбцов: "))
    if m<1 or n<1: 
        print("Параметры не могут быть отрицательными")
        exit(0)
except ValueError: 
    print("Параметры должны быть положительными целыми числами")
    exit(0)

mat = [[randint(-5, 5) for _ in range(n)] for i in range(m)]
for _ in mat:
    print(_)

new_sp = []
el_counter = {}

for stlb in range(0,n):                 #"разворачиваю" в одномерный список
    notnul = 0
    for strk in range(0,m):
        new_sp.append(mat[strk][stlb])

for item in new_sp:                     #словарь с элеметнами и их колличеством
    if item in el_counter:
        el_counter[item]+=1
    else:
        el_counter[item] = 1

uniq_sp = []
for item,count in el_counter.items():
    if count == 1: 
        uniq_sp.append(item)
print("Список неповторяющихся элементов: ",*uniq_sp)




    