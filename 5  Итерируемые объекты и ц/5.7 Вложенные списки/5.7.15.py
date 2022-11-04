'''A. Таблица умножения

Рассмотрим таблицу из n строк и n столбцов. Известно, что в клетке, образованной пересечением i-й строки и j-го столбца, записано число i × j. Строки и столбцы нумеруются с единицы.

Дано целое положительное число x. Требуется посчитать количество клеток таблицы, в которых находится число x.

Входные данные

В единственной строке находятся числа n и x (1 ≤ n ≤ 105, 1 ≤ x ≤ 109) — размер таблицы и число, которое мы ищем в таблице.

Выходные данные

Выведите единственное число: количество раз, которое число x встречается в таблице.'''

n, x = map(int, input().split())
s = 0
for i in range(1, n + 1):
    if x % i == 0 and x / i <= n:
        s += 1
print(s)
