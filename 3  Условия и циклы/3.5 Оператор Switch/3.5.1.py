'''Давайте попробуем потренироваться в операторе match-case

Чуть ранее студенты технических специальностей университета учились 5 лет (специалитет) и затем им вручался аттестат. Ваша программа программа будет получать на вход целое число - номер курса, и в зависимости от номера выводить следующий текст

если ввели 1, выведите сообщение Совсем еще зеленый студентик
если ввели 2, выведите сообщение Джун-студент
если ввели 3, выведите сообщение Мидл-студент
если ввели 4, выведите сообщение Сеньер-студент
если ввели 5, выведите сообщение Босс качалки
при вводе остальных значений, выведите текст Неизвестный курс
Используйте при решении оператор match-case'''

a = int(input())
match a:
    case 1:
        print('Совсем еще зеленый студентик')
    case 2:
        print('Джун-студент')
    case 3:
        print('Мидл-студент')
    case 4:
        print('Сеньер-студент')
    case 5:
        print('Босс качалки')
    case _:
        print('Неизвестный курс')
