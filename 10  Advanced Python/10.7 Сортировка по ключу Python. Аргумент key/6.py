'''Премия Оскар
Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет (Лео бы тогда давно купался в этих статуэтках)

Ваша задача написать программу, которая находит информацию, кто из актеров получил наибольшее и наименьшее количество статуэток

Входные данные
Программа принимать на вход в первой строке натуральное число n - количество вручаемых сегодня наград. И затем в n следующих строках вводятся имена актеров - победителей.

Выходные данные
Нужно вывести в  отдельных строках имена актеров набравших наибольшее и наименьшее количество статуэток и через запятую их количество. Гарантируется, что всегда будет только один человек, набравших наибольшее и наименьшее количество статуэток.'''

a = int(input())
d = {}
for i in range(a):
    c = input()
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
d = sorted(d.items(), key = lambda x: -x[1])
print(f'{d[0][0]}, {d[0][1]}', f'{d[-1][0]}, {d[-1][1]}', sep='\n')
