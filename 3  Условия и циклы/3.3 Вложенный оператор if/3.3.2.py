'''Даны три целых числа, каждое записано в отдельной строке.

Нужно вывести значение наибольшего из данных чисел

Примечание: используйте только условный оператор, функцией max пользоваться нельзя'''

a, b, c = int(input()), int(input()), int(input())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
