'''На вход поступает целое положительное число.

Программа должна вывести True, если у введенного числа последняя цифра 2, в противном случае - False.

Сделать задачу необходимо без использования условного оператора.'''

a = int(input())%10

print(not bool(a - 2))