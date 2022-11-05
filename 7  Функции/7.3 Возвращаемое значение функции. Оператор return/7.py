'''Ваша задача написать функцию format_name_list, которая принимает список словарей, у каждого словаря в этом списке есть только ключ name.

Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются запятой кроме последних двух имен, они должны быть разделены союзом "и". Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:

format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) => 'Bart, Lisa и Maggie'

format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) => 'Bart и Lisa'

format_name_list([{'name': 'Bart'}]) => 'Bart'

format_name_list([]) => ''
Ваша задача написать только определение функции format_name_list'''

def format_namelist(s):
    b = []
    c = ''
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return s[0]['name']
    else:
        for i in range(len(s)-2):
            b.append(s[i]['name'])
            c += s[i]['name'] + ', '
        return c + s[-2]['name'] + ' и ' + s[-1]['name']
        