"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def encode_decode(lst):
    for word in lst:
        word_as_bites = word.encode('utf-8')
        word_as_letters = word_as_bites.decode("utf-8")
        print(word_as_bites, word_as_letters)


lst_1 = ['разработка', 'администрирование', 'protocol', 'standard']
encode_decode(lst_1)