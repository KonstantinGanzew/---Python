'''Есть два словаря, нужно в словарь d2 вмержить словарь d1 при помощи метода update

В качестве ответа выведите словарь d2'''

d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
d2.update(d1)
print(d2)
