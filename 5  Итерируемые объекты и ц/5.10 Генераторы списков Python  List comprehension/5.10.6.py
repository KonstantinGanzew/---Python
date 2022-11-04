'''Создайте список первых букв каждого слова из строки st и выведите его на экран'''

st = 'Create a list of the first letters of every word in this string'.split()
a = [ i[0] for i in st ]
print(a)
