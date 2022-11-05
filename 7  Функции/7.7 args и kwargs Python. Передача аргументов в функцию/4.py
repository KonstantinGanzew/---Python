'''Напишите функцию only_one_positive, которая принимает произвольное количество числовых аргументов и возвращает True, когда из всех переданных значений только одно положительное, в противном случае верните False

Вам необходимо написать только определение функции only_one_positive

Ниже примеры вызова

only_one_positive(1, 2) -> False
only_one_positive(-1, 0, -3, 5, -3) -> True
only_one_positive() -> False'''

def only_one_positive(*args):
    count = 0
    for i in args:
        if i > 0:
            count += 1
            if count > 1:
                return False
    return False if count == 0 else True
    