'''Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

Входные данные
Входная строка может содержать содержит цифры, пробелы и латинские буквы.

Выходные данные
Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.'''

a = input()
s = set()
c = set()

for i in a:
    if i.isdecimal():
        if i in s:
            c.add(i)
        s.add(i)
c = sorted(list(c))
if len(c) != 0:
    print(*c)
else:
    print('NO')
    