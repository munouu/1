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

counter = 0

for stlb in range(0,n):
    notnul = 0
    for strk in range(0,m):
        if mat[strk][stlb]!=0:
            notnul+=1
    if m == notnul:
        counter+=1

print(counter)

    
