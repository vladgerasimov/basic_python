"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
  Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []

while True:
    new_item = input('Add an item')
    if new_item == 'stop':
        break
    else:
        my_list.append(new_item)

print(my_list)

n = 0
while True:
    try:
        my_list.insert(n, my_list[n+1])
        my_list.pop(n+2)
        n += 2
    except IndexError:
        break

print(my_list)
