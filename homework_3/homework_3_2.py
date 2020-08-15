"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
# name, surname, birth_year, city, mail, phone
def person_info(name, surname, birth_year, city, mail, phone):
    print(f'{name} {surname} {birth_year} года рождения, проживает в городе {city} email: {mail},'
          f'номер телефона {phone}')

person_info(name = 'Карина', surname = 'Магомедова,', birth_year = 1996, city = 'Москва', mail = 'sdadsad', phone = 999999)