'''Программа принимает на вход два слова s и t. 

Если слово t является словом s, записанным наоборот, выведите YES, иначе выведите NO.

Слова состоят из маленьких латинских букв. Входные данные не содержат лишних пробелов. Слова непустые, и их длины не превосходят 100 символов.'''

a = input()
b = input()
if a == b[::-1]:
    print('YES')
else:
    print('NO')
