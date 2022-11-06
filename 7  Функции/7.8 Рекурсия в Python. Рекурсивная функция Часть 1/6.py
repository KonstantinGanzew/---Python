'''Числа Трибоначчи
Описать рекурсивную функцию tribonacci, которая принимает на вход целое число n - порядковый номер чисел Трибоначчи. Функция по параметру n должна вычислить и вернуть значение, стоящее на n-м месте в ряде чисел Трибоначчи



Вот примере вызовов:

tribonacci(0) => 0
tribonacci(2) => 1
tribonacci(4) => 2
tribonacci(6) => 7
tribonacci(7) => > 13
Ваша задача только написать определение функции tribonacci'''

def tribonacci(n):
    return 0 if n < 2 else 1 if n == 2 else sum(tribonacci(n - i - 1) for i in range(3))
