"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

import os

file_name = 'my_file_2.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)

result = {}

with open(file_path) as my_file:
    total_lines = 0
    for line in my_file:
        total_lines += 1
        words_number = len(line.split(' '))
        result[f'В {total_lines} строке'] = f'{words_number} слов'

print(result)
