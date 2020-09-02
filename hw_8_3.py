"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyIntExc(Exception):
    def __init__(self, text='Тут не только числа'):
        self.text = text
        print(text)


def create_list():
    result = []
    while True:
        item = input('Введите элемент')
        if item == 'stop':
            break
        else:
            try:
                try:
                    result.append(int(item))
                except ValueError:
                    raise OnlyIntExc
            except OnlyIntExc:
                print('Нужно ввести число')
                pass
    return result


if __name__ == '__main__':
    print(create_list())
