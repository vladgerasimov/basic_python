"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.Необходимо построчно прочитать файл, вычислить
прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли
ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""

import json
import os

my_file_path = os.path.join(os.path.dirname(__file__), 'my_file_7.txt')
j_file_path = os.path.join(os.path.dirname(__file__), 'my_json_file_7.json')

data = []
result_dict = {}
average_dict = {}
result = []

with open(my_file_path, 'r', encoding='UTF-8') as file:
    companies_number = 0
    summary_profit = 0
    for line in file.readlines():
        data.append(line.split(' '))
        companies_number += 1
    for line in data:
        try:
            line[-1] = line[-1].rstrip()
        except ValueError:
            pass
        result_dict[line[0]] = int(line[-2]) - int(line[-1])
    result.append(result_dict)
    for i in result_dict:
        summary_profit += result_dict[i]

    average_dict['average_profit'] = round(summary_profit / companies_number)
    result.append(average_dict)

# j_result = json.dumps(result)

with open(j_file_path, 'w', encoding='UTF-8') as j_file:
    json.dump(result, j_file, ensure_ascii=False)
