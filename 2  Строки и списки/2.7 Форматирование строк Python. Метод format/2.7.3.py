'''Напишите программу, которая считывает целое число, и затем сообщает какие числа будут следующим и предыдущим в определенном формате. Пробелы, знаки препинания, заглавные и строчные буквы важны!'''

a = int(input())
b = str(a-1)
c = str(a+1)
print("Для числа {a} предыдущим будет число {b}.\nДля числа {a} следующим будет число {c}.".format(a=a, b=b, c=c))
