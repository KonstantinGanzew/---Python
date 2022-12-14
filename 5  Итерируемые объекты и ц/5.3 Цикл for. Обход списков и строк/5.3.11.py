'''Правильная скобочная последовательность
Одна из стандартных задач на программирование. Подумайте над способом ее решения, если не приходит ничего в голову, загляните в подсказку)

И так, у нас есть последовательность скобочных символов, состоящая только из символов ( и )

Ваша задача определить является ли введенная скобочная последовательность правильной.

Правильная скобочная последовательность (ПСП) называется строка, состоящая только символов "скобок", где каждой закрывающей скобке найдётся соответствующая открывающая. При этом учитывайте, что:

Пустая последовательность является правильной.
Если A – правильная скобочная последовательность, то (A) – правильные скобочные последовательности.
Если A и B – правильные скобочные последовательности, то AB – правильная скобочная последовательность.
Если введенная строка является ПСП, выведите YES, в противном случае - NO.'''

pairs = {'()', '[]', '{}'}    
str = input().replace(' ', '')
for _ in range(len(str)//2):
    for i in pairs:
        str = str.replace(i, '')
if len(str)==0:
    print('YES')
else:
    print('NO')
