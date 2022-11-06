'''Быстрая сортировка (quick sort) | Разбор

Быстрая сортировка - еще один вид сортировки, который использует рекурсию. 



Ваша задача реализовать этот алгоритм. Для этого нужно будет создать функцию quick_sort, которая будет принимать исходный список и возвращать новый отсортированный в порядке неубывания список.

Необходимо написать только определение функций quick_sort, при этом нельзя пользоваться встроенными сортировками в Python'''

def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))
    return quick_sort(left) + center + quick_sort(right)
