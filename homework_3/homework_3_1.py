"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_division(a, b):
    while True:
        try:
            a = float(input('Введите делимое'))
            break
        except ValueError:
            print('Необходимо число')
    while True:
        try:
            b = float(input('Введите делитель'))
            if b == 0:
                print('На ноль делить нельзя')
                continue
            break
        except ValueError:
            print('Необходимо число')
    return a / b


print(my_division(2, 3))
