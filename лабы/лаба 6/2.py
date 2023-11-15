string = input("Введите свое сочинение: ")

print(f'Ваша строка: {string}')

string+=' '
ind = 0
string_1 = []

for el in range(0,len(string)): 
    if string[el] in ';,. ':
        string_1+=[string[ind:el]]
        ind=el

ind = 0
counter = 0

for el in string_1:
    if el != ' ' and el != '.' and el != ';' and el != ',':
        counter+=1


print(counter)


