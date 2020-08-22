"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""


import os

file_path = os.path.join(os.path.dirname(__file__), 'my_file_5.txt')

with open(file_path, 'w', encoding='UTF-8') as my_file:
    my_file.write(input('Введите числа через пробел'))

with open(file_path, 'r', encoding='UTF-8') as my_file:
    data = my_file.read().split(' ')
    for idx, i in enumerate(data):
        data[idx] = int(i)
    print(f'Сумма чисел составляет {sum(data)}')