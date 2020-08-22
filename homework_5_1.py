"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

import os

file_name = 'my_file_1.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)

with open(file_path, 'w') as my_file:
    while True:
        new_string = input('Введите строки')
        my_file.write(new_string + '\n')
        if new_string == '':
            print('Ввод данных закончен')
            break
