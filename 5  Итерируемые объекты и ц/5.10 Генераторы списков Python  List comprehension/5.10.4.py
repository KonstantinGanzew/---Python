'''При помощи list comprehension создайте список, состоящий из нечетных натуральных чисел в интервале [ nn; n^2n 
2
  ] и вывести его на экран. Само число nn поступает на вход программе

Формат ввода
Вводится натуральное число nn. 

Формат вывода
Вывести список, содержащий нечетные натуральные числа в интервале  [ nn; n^2n 
2
  ]'''

n = int(input())
a = [ i for i in range(n, n**2+1) if i % 2 != 0 ]
print(a)
