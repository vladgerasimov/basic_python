"""Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'my_file_4.txt')
new_file_path = os.path.join(os.path.dirname(__file__), 'my_file_4_new.txt')
data = []

with open(file_path, 'r', encoding='UTF-8') as my_file:
    for line in my_file.readlines():
        data.append(line.split(' '))

init_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

for i in data:
    if i[0] == 'One':
        i[0] = init_dict['One']
        data[0] = ' '.join(i)
    elif i[0] == 'Two':
        i[0] = init_dict['Two']
        data[1] = ' '.join(i)
    elif i[0] == 'Three':
        i[0] = init_dict['Three']
        data[2] = ' '.join(i)
    elif i[0] == 'Four':
        i[0] = init_dict['Four']
        data[3] = ' '.join(i)

print(data)

with open(new_file_path, 'w', encoding='UTF-8') as my_new_file:
    my_new_file.writelines(data)
