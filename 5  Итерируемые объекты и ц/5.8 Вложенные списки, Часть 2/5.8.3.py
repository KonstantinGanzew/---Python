'''Заполнение змейкой

Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.'''

a, b = map(int, input().split())
k = 0
c = []
for i in range(a):
    s = []
    for j in range(b):
        s.append(k)
        k += 1
    c.append(s)

for i in range(a):
    if i % 2 == 0:
        for j in range(b):
            print(c[i][j], end=' ')
    else:
        for j in range(b-1, -1, -1):
            print(c[i][j], end=' ')
    print()
