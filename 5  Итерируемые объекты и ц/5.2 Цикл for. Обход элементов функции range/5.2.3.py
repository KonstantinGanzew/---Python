'''Программа принимает на вход натуральное число N. Ваша задача вывести на экран все числа от N до 1 в сторону уменьшения каждое число на отдельной строке. '''

a = int(input())
for i in range(a, 0, -1):
    print(i)
