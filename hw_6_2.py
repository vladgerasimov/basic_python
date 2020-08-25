"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
"""


class Road:
    _length = 0
    _width = 0
    mass_per_m = 25

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def caclulate_mass(self, deep):
        return self.length * self.width * self.mass_per_m * deep


my_road = Road(5000, 20)
print(my_road.caclulate_mass(5))