from numpy import *

count = int(input("длина списка: "))

sp = []
lo = -5
hi = 20

for _ in range(1,count+1):
    sp+=[random.randint(lo,hi)]
print(sp)


