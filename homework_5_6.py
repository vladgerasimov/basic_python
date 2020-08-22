"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету
и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'my_file_6.txt')

data = []

result = {}

with open(file_path, 'r', encoding='UTF-8') as my_file:
    for line in my_file.readlines():
        data.append(line.split(' '))
    for line in data:
        for idx, string in enumerate(line):
            line[idx] = string.rstrip('(лпрлаб\n-)')
        for idx, string in enumerate(line[1:], start=1):
            try:
                line[idx] = int(string)
            except ValueError:
                pass
        for idx, string in enumerate(line[1:], start=1):
            try:
                line.remove('')
            except ValueError:
                pass
        result[line[0]] = sum(line[1:])
    print(data)
    print(result)
