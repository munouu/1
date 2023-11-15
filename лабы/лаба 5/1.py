import sys
try:
    a = float(input("Введите возводимое в степень дейстительное число: "))
except ValueError: 
    print("\n","Вы ввели некорректное значение","\n","Попробуйте снова","\n")
    sys.exit()

try:
    n = int(input("Введите целое число степени: "))
    if n<=0: print("\n","Значение степени должно быть положительным","\n")
except ValueError: 
    print("\n","Вы ввели некорректное значение","\n","Попробуйте снова","\n")
    sys.exit()

for i in range(1,n+1):
    print(a**i)
