'''Программа получает на вход одно слово. Ваша задача перенести последнюю букву в начало, тем самым сдвинуть все остальные буквы вправо на один разряд. В качестве ответа нужно вывести полученное слово'''

a = input()
print(a[-1]+a[:-1])
