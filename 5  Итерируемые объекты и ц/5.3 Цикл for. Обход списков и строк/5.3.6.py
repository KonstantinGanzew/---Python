'''Линейный поиск
Линейный поиск, также известный как последовательный поиск, этот метод используется для поиска элемента в списке. Линейный поиск является одним из базовых алгоритмов, с которым вы должны познакомиться, изучая программирования. Суть алгоритма в следующем: вы должны проверять каждый элемент списка последовательно один за другим, пока не найдете интересующий вас элемент или пока не закончится весь список.

Входные данные
Программа получает на вход в одной строке элементы списка - целые числа, разделенные пробелом. Количество элементов произвольное

И на следующей строке вводится одно число r - значение поиска

Выходные данные
Ваша задача реализовать линейный алгоритм поиска введенного значения r. В случае успеха - выведите порядковый номер(индекс) первого найденного элемента в списке при условии, что индексация начинается с единицы. Если данный элемент отсутствует - необходимо вывести строку ErrorValue '''

a = list(map(int, input().split()))
b = int(input())
c = 0
t = False
for i in range(len(a)):
    if b == a[i]:
        t = True
        break
    c += 1
if t:
    print(c+1)
else:
    print('ErrorValue')
