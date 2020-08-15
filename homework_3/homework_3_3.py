"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_max(some_list):
    result = None
    for i in some_list:
        if result is None:
            result = i
        elif i > result:
            result = i
    return result


def my_func(a, b, c):
    numbers = [a, b, c]
    max_num1 = my_max(numbers)
    numbers.remove(max_num1)
    max_num2 = my_max(numbers)
    return max_num1 + max_num2


print(my_func(1, 1, 10))
