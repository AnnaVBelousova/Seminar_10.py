"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet


def ping_function(lst):
    YA_PING = subprocess.Popen(lst, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        result = chardet.detect(line)
        keys_list = list(result.keys())
        key_1 = keys_list[0]
        line = line.decode(result[key_1]).encode('utf-8')
        print(line.decode('utf-8'))
        # print(result)


ARGS = ['ping', 'yandex.ru']
ARGS_2 = ['ping', 'youtube.ru']

ping_function(ARGS)
ping_function(ARGS_2)