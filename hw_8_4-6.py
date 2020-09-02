"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""
from typing import Dict


class Warehouse:
    warehouse_dict = {
        'printers': 0,
        'scanners': 0,
        'xeroxes': 0
    }

    @staticmethod
    def show_info():
        print(f'На складе {Warehouse.warehouse_dict["printers"]} принтеров, {Warehouse.warehouse_dict["scanners"]} '
              f'сканеров и {Warehouse.warehouse_dict["xeroxes"]} ксероксов')


class Equipment:
    total_dict: Dict[str, int] = {
        'printers': 0,
        'scanners': 0,
        'xeroxes': 0
    }


class Printer(Equipment):
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        super(Printer, self).total_dict['printers'] += self.number

    def to_warehouse(self, number: int):
        if self.total_dict['printers'] < number:
            print(f'В офисе всего {self.total_dict["printers"]} принтеров')
        else:
            super(Printer, self).total_dict['printers'] -= number
            self.number -= number
            Warehouse.warehouse_dict['printers'] += number
            print(f'{number} принтеров отправлены на склад')

    def from_warehouse(self, number: int):
        if Warehouse.warehouse_dict['printers'] < number:
            print(f'На складе всего {Warehouse.warehouse_dict["printers"]} принтеров')
        else:
            super(Printer, self).total_dict['printers'] += number
            self.number += number
            Warehouse.warehouse_dict['printers'] -= number
            print(f'{number} принтеров возвращены со склада')

    def __str__(self):
        return f'Принтеры: в офисе - {self.number}, на складе - {my_warehouse.warehouse_dict["printers"]}'


class Scanner(Equipment):
    def __init__(self, number: int, power: int):
        self.number = number
        self.power = power
        super().total_dict['scanners'] += self.number

    def to_warehouse(self, number: int):
        if self.total_dict['scanners'] < number:
            print(f'В офисе всего {self.total_dict["scanners"]} сканеров')
        else:
            super(Scanner, self).total_dict['scanners'] -= number
            self.number -= number
            Warehouse.warehouse_dict['scanners'] += number
            print(f'{number} сканеров отправлены на склад')

    def from_warehouse(self, number: int):
        if Warehouse.warehouse_dict['scanners'] < number:
            print(f'На складе всего {Warehouse.warehouse_dict["scanners"]} сканеров')
        else:
            super(Scanner, self).total_dict['scanners'] += number
            self.number += number
            Warehouse.warehouse_dict['scanners'] -= number
            print(f'{number} сканеров возвращены со склада')

    def __str__(self):
        return f'Сканеры: в офисе - {self.number}, на складе - {my_warehouse.warehouse_dict["scanners"]}'


class Xerox(Equipment):
    def __init__(self, number: int, speed: int):
        self.number = number
        self.speed = speed
        super().total_dict['xeroxes'] += self.number

    def to_warehouse(self, number: int):
        if self.total_dict['xeroxes'] < number:
            print(f'В офисе всего {self.total_dict["xeroxes"]} ксероксов')
        else:
            super(Xerox, self).total_dict['xeroxes'] -= number
            self.number -= number
            Warehouse.warehouse_dict['xeroxes'] += number
            print(f'{number} ксероксов отправлены на склад')

    def from_warehouse(self, number: int):
        if Warehouse.warehouse_dict['xeroxes'] < number:
            print(f'На складе всего {Warehouse.warehouse_dict["xeroxes"]} ксероксов')
        else:
            super(Xerox, self).total_dict['xeroxes'] += number
            self.number += number
            Warehouse.warehouse_dict['xeroxes'] -= number
            print(f'{number} ксероксов возвращены со склада')

    def __str__(self):
        return f'Ксероксы: в офисе - {self.number}, на складе - {my_warehouse.warehouse_dict["xeroxes"]}'


my_warehouse = Warehouse()
printer = Printer(20, 300)
scanner = Scanner(50, 200)

printer.to_warehouse(10)
print(1)
