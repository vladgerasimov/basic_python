"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker_1 = Position('Иван', 'Иванов', 'Инженер', 50000, 20000)

worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position('Матвей', 'Кудрин', 'Ведущий Инженер', 150000, 30000)

worker_2.get_full_name()
worker_2.get_total_income()
