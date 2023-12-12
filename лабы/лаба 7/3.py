geo_dict = {
    "Россия":['Москва','Калининград','Крснодар','Екатеринбург','Ярославль','Омск','Псков'],
    "США":['Чикаго','Даллас','Хьюстон','Вашингтон','Сиэтл','Нашвилл']}


while True:
    city = input("Введите город: ")
    city = city.upper()[0]+city.lower()[1:]
    for country in geo_dict.keys():
        if city in geo_dict[country]:
            print(f'Город {city} находится в стране {country}')
            break



