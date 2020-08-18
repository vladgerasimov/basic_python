"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
 для конкретных значений необходимо запускать скрипт с параметрами.
 """

from sys import argv


def salary_calc(hours, rate_hour, bonus):
    return (hours * rate_hour) + bonus


good_data = True
_, *args = argv

for idx, i in enumerate(args):
    try:
        args[idx] = float(i)
    except ValueError:
        print('Ошибка ввода')
        good_data = not good_data
        break

if good_data:
    print(salary_calc(*args))
else:
    print('Введите числа по порядку через пробел: выработка, ставка, премия')
