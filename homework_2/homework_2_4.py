"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_string = input('Enter your string')

try:
    user_list = user_string.split(' ')
except:
    print('There must be spaces in a string')

n = 1

for item in user_list:
    print(n, '-', item[:10])
    n += 1
