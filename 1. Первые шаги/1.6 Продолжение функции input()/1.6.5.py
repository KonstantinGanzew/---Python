'''Магазин канцелярских товаров
Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров. Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера. Также известно, что стоимость карандаша составляет 3 рубля. Требуется определить общую стоимость покупки.'''

a, b, c = map(int, input().split())

print(a * 3 + b * 5 + c * 12)