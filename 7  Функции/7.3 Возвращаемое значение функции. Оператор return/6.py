'''Напишите функцию first_unique_char, которая принимает строку символов и возвращает целое число: позицию первого уникального символа в строке. В случае, если уникальных символов в переданной строке нет, верните -1. Регистр символов не учитывайте.

Ваша задача написать только определение функции first_unique_char'''

def first_unique_char(x):
    a = 0
    for i in x:
        if x.count(i) == 1:
            a = x.index(i)
            break
        else:
            a = -1
    return a
