"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()."""


def int_func(word=str):
    if word.islower():
        first_letter = str(word[0]).upper()
        word = first_letter + word[1:]
    else:
        print('Все буквы слова должны быть в нижнем регистре')
        return
    return word


print(int_func('hello'))


def main_func(string=str):
    my_list = str(string).split(' ')
    result = []
    try:
        for i in my_list:
            i = int_func(i)
            result.append(i)
        string = ' '.join(result)
        return string
    except TypeError:
        return


print(main_func('Hello world'))
