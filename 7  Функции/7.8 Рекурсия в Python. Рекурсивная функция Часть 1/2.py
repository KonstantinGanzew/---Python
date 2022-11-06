'''Определите функцию print_to, которая принимает одно натуральное число n и распечатывает на экране последовательность целых чисел от 1 до n включительно. Каждое число необходимо выводить на отдельной строке. 

Ваша задача только написать определение функции print_to'''

def print_to(n: int) -> None:
    if n != 1:
        print_to(n-1)
    print(n)
