"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы
должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print('Отрисовка маркером')


pen = Pen()
pen.draw()
print(pen.title)

pencile = Pencil()
pencile.draw()
print(pencile.title)

handle = Handle()
handle.draw()
print(handle.title)

