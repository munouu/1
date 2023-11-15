string = input("Введите свое сочинение: ")
counter = 0

for el in string:
    if el in "  ,   ;. ":
        counter+=1
print(counter)
