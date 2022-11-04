'''Спираль

Требуется вывести квадрат, состоящий из N×N клеток, заполненных числами от 1 до N2 по спирали (см. примеры).

Входные данные
Программа получает на вход одно число n.

Выходные данные
Программа должна вывести матрицу, заполненную числами от 1 до N2 по спирали, при этом между числами может быть любое количество пробелов. Не допускается начинать спираль в ином, кроме верхнего левого, углу, закручивать спираль против часовой стрелки или изнутри наружу.'''

n = int(input())
mas = [[0]*n for i in range(n)]
i = 1
x = 0
y = -1
d_row = 0
d_colum = 1
lenght = len(str(n**2))
while i <= n**2:
    if 0 <= x + d_row < n and 0 <= y + d_colum < n and mas[x + d_row][y + d_colum]==0:
        x+=d_row
        y+=d_colum
        mas[x][y]=i
        i += 1
    else:
        if d_colum==1:
            d_colum = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_colum = -1
        elif d_colum == -1:
            d_colum = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_colum = 1
for row in mas:
    for elem in row:
        print(str(elem).rjust(lenght), end=' ')
    print()
