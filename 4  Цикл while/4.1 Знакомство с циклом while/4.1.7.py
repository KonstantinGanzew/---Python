'''В первый день спортсмен пробежал X километров. В каждый последующий день он увеличивал пробег на 15% от предыдущего дня. Вам необходимо определить номер дня, в который пробег спортсмена составил не менее Y километров. Само число Y будем поступать на вход программе.'''

a, b = map(int, input().split())
c = 1
while a <= b:
    a += a/100*15
    c += 1
print(c)
