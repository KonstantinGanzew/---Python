'''Мы уже с вами подсчитывали сколько раз встречается число в списке при помощи метода подсчета. Там мы использовали список для хранения найденного количества

Теперь ваша задача научиться использовать словарь для подсчета количества. Вашей программе поступает на вход строка, вам необходимо подсчитать сколько раз встретилась каждая буква в этой строке без учета регистра, при этом цифры и символы пунктуации нужно пропустить. Ответ нужно сохранить в словаре, в котором ключ - буква, а значение - количество раз, сколько эта буква встретилась в строке. В качестве ответа нужно вывести словарь
'''

a = input().lower()
d = {}
for s in a:
    if s.isalpha():
        d[s] = d.get(s, 0)+1
print(d)
