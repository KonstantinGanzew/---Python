'''Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится "соль". Переписывайте без этого слова.

Формат ввода
На первой строке вводится натуральное число N — количество пунктов рецепта.
Далее следуют N строк — пункты рецепта.

Формат вывода
Одна строка — пункты рецепта, разделённые запятой и пробелом, без пунктов с упоминанием слова "соль" (то есть таких, в которых нет подстроки "соль" в нижнем регистре).'''

a = int(input())
c = ''
for i in range(a):
    s = input()
    if 'соль' in s:
        continue
    else:
        c += s + ', '        
print(c[:-2])
