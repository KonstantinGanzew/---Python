'''Напишите программу, которая проверяет начинается ли введенная фраза строкой mam вне зависимости от регистра букв

В качестве ответа необходимо вывести True, если введенная строка начинается с mam, во всех остальных случаях нужно вывести False'''

s = input().lower()
print(s.startswith('mam'))
