string = input("Введите свое сочинение: ")

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
print('Ну хоть что-нибудь введи' if string == ' ' else ('Колличество слов в ваших писаках: ', counter))

#print('\n',f'Ваш труд: {string}\n Колличество слов в ваших писаках: {counter}','\n')


