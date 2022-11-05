'''Снова НОД
В этой задаче вам необходимо воспользоваться уже готовой функцией gcd(a, b), которая принимает два числа и находит наибольших общий делитель для них.

Ваша задача при помощи функции gcd определить НОД произвольного количества чисел.

Входные данные
На первой строке вводится натуральное число n – количество чисел. Далее идут n строк, в каждой из которых натуральное число.

Выходные данные
НОД введенных чисел.'''

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a
n = int(input())
c = []
for i in range(n):
    c.append(int(input()))
print(gcd(min(c), max(c)))
