'''Вам нужно посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.

Под главной диагональю матрицы подразумевается диагональ, проведённая из левого верхнего угла в правый нижний.

Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, а затем в N строках записаны элементы списка.'''

a = int(input())
b = []
for i in range(a):
    b.append(list(map(int, input().split())))
s = 0
for i in range(a):
    for j in range(a):
        if i == j:
            s += b[i][j]
print(s)
