'''Программа запрашивает у пользователя курс доллара - вещественное число,  и также количество долларов(целое число), которое пользователь хочет приобрести. В итоге программа должна вывести следующее сообщение:

"Current dollar rate is <курс доллара>. You want buy <количество долларов> dollars
You must pay <стоимость>"'''

a = float(input())
b = int(input())
print(f"Current dollar rate is {a}. You want buy {b} dollars\nYou must pay {a * b}")