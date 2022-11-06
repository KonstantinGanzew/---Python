'''Рейтинг таксистов
Руководитель таксопарка хочет увидеть отчет по всем таксистам, где нужно указать имя таксиста и его среднюю оценку. Информацию в отчете нужно расположить по убыванию средней оценки таксиста.

После каждого успешно выполненного заказа, клиент выставляет таксисту оценку - целое число от 1 до 5.

Входные данные
Программа будет принимать строки, в которых сперва указывается имя таксиста, а затем через запятую с пробелом его оценка за заказ.

Строка "конец" является последней строкой и означает окончание ввода

Выходные данные
Нужно расположить таксистов в порядке убывания их средней оценке и вывести имя каждого таксиста и его среднюю оценку в отдельной строке. В случае совпадения средних оценок расположить таксистов нужно отсортировать имена таксистов по алфавиту '''

d = {}

a = input()
while a != 'конец':
    c = a.split(', ')
    if c[0] in d:
        d[c[0]][0] += int(c[1])
        d[c[0]][1] += 1
    else:
        d[c[0]] = [int(c[1]), 1]
    a = input()

for i in sorted(d.items(), key=lambda x: (-(x[1][0]/x[1][1]), x[0])):
    print(i[0], i[1][0]/i[1][1])
