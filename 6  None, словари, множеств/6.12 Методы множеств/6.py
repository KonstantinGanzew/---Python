'''Даны два списка чисел.

Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.'''

a, b = set(map(int, input().split())), set(map(int, input().split()))
c = sorted(list(a.intersection(b)))
print(*c)
