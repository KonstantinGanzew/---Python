'''На вход поступают два целых числа.

Программа должна вывести True, если оба числа делятся на 7, в противном случае - False.

Сделать задачу необходимо без использования условного оператора.'''

a, b = map(int, input().split())

print(not bool(a%7) and not bool(b%7))