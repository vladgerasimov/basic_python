"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivExc(Exception):
    def __init__(self, text='Невозможно разделить на 0'):
        self.text = text
        print(text)


def divide():
    a = float(input('Введите делимое'))
    b = float(input('Введите делитель'))
    try:
        if b == 0:
            raise ZeroDivExc
        print(a / b)
    except ZeroDivExc as err:
        print(err)
        pass
    except ValueError:
        print('Введите числа')


if __name__ == '__main__':
    divide()
