"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, my_date: str):
        self.__my_date = str(my_date)

    @classmethod
    def get_int_date(cls, str_date: str):
        str_date = str(str_date).split('-')
        for idx, item in enumerate(str_date):
            str_date[idx] = int(item)
        return str_date

    @staticmethod
    def verify_date(date):
        date = Date.get_int_date(date)
        if 1 <= date[0] <= Date.months[date[1]] and 1 <= date[1] <= 12 and date[2] > 0:
            return True
        else:
            return False


date_1 = '11-11-1997'
date_2 = '19-08-1994'
date_3 = '30-02-2020'
date_4 = '10-10-0'

if Date.verify_date('11-11-11'):
    print('This is a quite good date')
else:
    print('Eew it is not that good actually')

if Date.verify_date('44-11-11'):
    print('This is a quite good date')
else:
    print('Eew it is not that good actually')

print(Date.verify_date(date_1))
print(Date.verify_date(date_2))
print(Date.verify_date(date_3))
print(Date.verify_date(date_4))
