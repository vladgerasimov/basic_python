"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_raise_degree(x=float, y=int):
    return x ** y


print(my_raise_degree(2, -2))


def my_raise_degree2(x=float, y=int):
    result = None
    iteration_number = 1
    while iteration_number < abs(y):
        if result is None:
            result = 1 / x
        else:
            result *= 1/x
            iteration_number += 1
    return result

print(my_raise_degree2(2, -2))