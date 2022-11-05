'''В этой задаче вам предстоит достать определенные данные из словаря data. Он уже будет определен и заполнен данными, поэтому никакого ввода значений в это программе делать не нужно, просто обращаетесь к переменной data

У словаря data следующая структура ключей, хорошо рассмотрите ее.

{
  "my_friends": {
    "count": ...,
    "people": [
      {
        "first_name": value,
        "id": value,
        "last_name": value,
      },
      {
        "first_name": value,
        "id": value,
        "last_name": value,
      }, 
      ......
    ]
  }
}
Ваша задача получить значения ключа first_name у всех элементов и вывести их в алфавитном порядке, каждое имя с новой строки

P.S. Чтобы посмотреть содержимое словаря data воспользуйтесь следующим кодом:

from pprint import pprint
pprint(data)'''

data = {'my_friends': {'count': 10,
                'people': [{'bdate': '31.8.2005',
                            'first_name': 'Kurt',
                            'id': 621547005,
                            'last_name': 'Cobain'},
                           {'first_name': 'Виолетта',
                            'id': 484200150,
                            'last_name': 'Кастилио'},
                           {'bdate': '28.8.1942',
                            'first_name': 'Иринка',
                            'id': 21886133,
                            'last_name': 'Бушуева'},
                           {'bdate': '4.7.2002',
                            'first_name': 'Данил',
                            'id': 282456573,
                            'last_name': 'Греков'},
                           {'bdate': '25.5',
                            'first_name': 'Валентин',
                            'id': 184902932,
                            'last_name': 'Долматов'},
                           {'bdate': '6.12.1982',
                            'first_name': 'Евгений',
                            'id': 620469646,
                            'last_name': 'Шапорин'},
                           {'bdate': '4.11.1995',
                            'first_name': 'Ангелина',
                            'id': 622328862,
                            'last_name': 'Краснова'},
                           {'bdate': '2.2.1915',
                            'first_name': 'Иван',
                            'id': 576015198,
                            'last_name': 'Вирин'},
                           {'bdate': '27.9',
                            'first_name': 'Паша',
                            'id': 386922406,
                            'last_name': 'Воронов'},
                           {'bdate': '20.12',
                            'first_name': 'Ольга',
                            'id': 622170942,
                            'last_name': 'Савченкова'}]}}

name = []
for i in data['my_friends']['people']:
    name.append(i['first_name'])
name.sort()
for i in name:
    print(i)
