"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def convert_to_bytes_format(lst):
    for word in lst:
        print(
            f"байтовый формат: {bytes(word, 'utf-8')}\nтип переменных: {type(bytes(word, 'utf-8'))}\nдлина переменных:{len(bytes(word, 'utf-8'))}"),
        print(f"содержимое переменных:")
        for char in bytes(word, 'utf-8'):
            print(char, end=' ')
        print(sep='\n')
        print(sep='\n')


lst_1 = ['class', 'function', 'method']
convert_to_bytes_format(lst_1)