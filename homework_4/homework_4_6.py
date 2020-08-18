"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
"""
from sys import argv
import itertools


def my_count(init_number):
    my_list = []
    for i in itertools.count(init_number):
        if len(my_list) > 20:
            break
        else:
            my_list.append(i)
    return my_list


def my_cycle(*args):
    my_list2 = args
    my_result = []
    for i in itertools.cycle(my_list2):
        if len(my_result) <= 20:
            my_result.append(i)
        else:
            return my_result


_, command, *args = argv

menu = {
    'count': my_count,
    'cycle': my_cycle
}

if command == 'count':
    for idx, i in enumerate(args):
        args[idx] = int(i)

result = menu[command](*args)


print(result)