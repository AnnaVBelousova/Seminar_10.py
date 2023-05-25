"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def exeption_words(lst):
    for word in lst:
        # word_as_bytes = bytes(word, "utf-8" )
        try:
            if len(bytes(word, "utf-8")) != len(word):
                res = f'слово "{word}" невозможно записать в байтовом типе c помощью маркировки b'''
                print(res)
            else:
                raise ValueError
        except:
            # print( ValueError(f'слово "{word}" можно записать в байтовом типе c помощью маркировки b'''))
            print()


lst_1 = ['attribute', 'класс', 'функция', 'type']
exeption_words(lst_1)