'''Программа принимает на вход одно натуральное число. Ваша задачи найти сколько раз встречается цифра 7 в этом числе'''

a = int(input())
c = 0
while a > 0:
    if a % 10 == 7:
        c += 1
    a //= 10
print(c)
