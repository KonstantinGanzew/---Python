'''Ваша программа получает на вход возраст человека. Вам необходимо вывести на экран сообщение:

"Младенец", если возраст меньше 2х лет;
"Малыш", если возраст от 2, но меньше 4;
"Ребенок", если возраст от 4 лет, но меньше 12;
"Подросток", когда возраст от 12 лет, но меньше 19;
"Взрослый человек", когда возраст от 19 лет, но меньше 65;
"Пожилой человек", если возраст 65 и более.'''

a = int(input())
if a < 2:
    print('Младенец')
elif 2 <= a < 4:
    print('Малыш')
elif 4 <= a < 12:
    print('Ребенок')
elif 12 <= a < 19:
    print('Подросток')
elif 19 <= a < 65:
    print('Взрослый человек')
else:
    print('Пожилой человек')
