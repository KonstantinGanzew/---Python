'''Программа получает на вход натуральное число N. 

Нужно найти сумму его делителей. '''

a = int(input())
c = 1
s = []
while c*c <= a:
    if a % c == 0:
        s.append(c)
        if c != a // c:
            s.append(a // c)
    c += 1
print(sum(s))
