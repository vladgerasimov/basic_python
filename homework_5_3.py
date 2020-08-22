"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'my_file_3.txt')

low_revenue = []
total_revenue = 0

with open(file_path, 'r', encoding='UTF-8') as my_file:
    count = 1
    for line in my_file.readlines():
        surname = line.split(' ')[0]
        revenue = int(line.split(' ')[1])
        if revenue < 20000:
            low_revenue.append(surname)
        total_revenue += revenue
        count += 1

average_revenue = total_revenue / count

print(f'Низкая зарплата у: {" ".join(low_revenue)}, средняя зарплата составляет {round(average_revenue, 2)}')
