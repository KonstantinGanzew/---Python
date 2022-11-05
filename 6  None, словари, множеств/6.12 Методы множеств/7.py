'''Даны два списка чисел. Выведите все числа в порядке возрастания, которые входят в первый список, но при этом отсутствуют во втором. '''

a, b = set(map(int, input().split())), set(map(int, input().split()))
c = sorted(list(a.difference(b)))
print(*c)
