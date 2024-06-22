# Работа со словарями
my_dict = {'Оля': 1994 , 'Света': 1999 , 'Вика': 2001}
print(my_dict)
print(my_dict['Оля'], my_dict.get('Лиза'))
my_dict.update({'Настя': 2002,
                'Катя': 1996})
someone = my_dict.pop('Оля')
print(someone)
print(my_dict)

# Работа с множествами
my_set = {1 , 2 , 2 , 3, 'Один', 'Два', 'Один', True}
print(my_set)
my_set.update({'Три', 'Четыре'})
print(my_set.remove('Один'))
print(my_set)