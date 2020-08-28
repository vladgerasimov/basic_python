"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""

import random


class Matrix:

    def __init__(self, my_data: list = 0):
        # Проверяю, что число элементов в строках матрицы совпадает, если переданы данные при создании экземпляра
        if my_data:
            self.line_length = len(my_data[0])
            for i in my_data:
                if len(i) != self.line_length:
                    raise ValueError('Длины строк не совпадают')
        # Добавляю введенные данные в атрибут элементов матрицы
        self.matrix_items = my_data if my_data else [[random.randint(1, 15), random.randint(1, 15),
                                                      random.randint(1, 15)] for _ in range(3)]

    def __str__(self):
        result = ''
        # Преобразование каждой строки матрицы к типу данных строка, добавление строки в возвращаемый результат
        for line in self.matrix_items:
            result = result + '\n' + '  '.join(str(i) for i in line)
        return result

    def __add__(self, other):
        # Складываю соответствующие элементы двух матриц, сохраняю все это в список, возвращаю экземпляр
        # класса матрица, передав в него полученный список
        result = []
        for line_idx, line in enumerate(self.matrix_items):
            result.append([])
            for item_idx, item in enumerate(line):
                line[item_idx] = int(item)
                pre_result = self.matrix_items[line_idx][item_idx] + other.matrix_items[line_idx][item_idx]
                result[line_idx].append(pre_result)
        return Matrix(result)


m = Matrix([[1, 2, 5], [3, 6, 8], [4, 6, 7]])
m_2 = Matrix([[1, 3, 1], [4, 7, 8], [2, 10, 11]])
m_3 = Matrix()
m_4 = Matrix()

print(m)
print(m_2)
print(m_3+m_4)
print(m + m_2)
