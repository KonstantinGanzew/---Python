'''Вот мы с вами и добрались до легендарной сортировки пузырьком. 



Все просто, вам поступает число n - количество элементов в списке, и затем сам список.

Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки, в случае если элементы соседние совпадают менять их ненужно.

В качестве ответа нужно вывести отсортированный список и какое количество раз пришлось переставлять элементы в процессе сортировки'''

a = int(input())
b = list(map(int, input().split()))
e = 0
for i in range(a-1):
    for j in range(a-i-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
            e += 1
print(*b)
print(e)
