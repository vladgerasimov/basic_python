"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

#1st way

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    try:
        user_month = int(input('Enter a month'))
        if not 1 <= user_month <= 12:
            print('Enter an INTEGER 1-12')
        else:
            break
    except ValueError:
        print('Enter an INTEGER 1-12')

if user_month in months[:2] or user_month == months[11]:
    print('This is winter')
elif user_month in months[2:5]:
    print('This is spring')
elif user_month in months[5:8]:
    print('This is summer')
else:
    print('This is autumn')

#2nd way

months = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7:'summer',
8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'}

while True:
    try:
        user_month = int(input('Enter a month'))
        if not 1 <= user_month <= 12:
            print('Enter an INTEGER 1-12')
        else:
            break
    except ValueError:
        print('Enter an INTEGER 1-12')

print(f'This is {months[user_month]}')