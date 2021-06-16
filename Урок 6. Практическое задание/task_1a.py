"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""


import memory_profiler
from timeit import default_timer


def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return res, mem_diff, time_diff
    return wrapper
@decor
def splitter(string):
    splitter_list = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] != string:
                splitter_list.append(hash(string[i:j]))
    return set(splitter_list)


res3, mem_diff3, time_diff3 = splitter('fasl;dfkjasdoij;oierjf;oijf;asdfjqwrqeoqawepokpokpolka;ldfkasdlkf')
print(f'выполнение заняло {mem_diff3} MiB и {time_diff3} секунд')


@decor
def splitter_two(string):
    splitter_list = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] != string:
                splitter_list.append(hash(string[i:j]))
                yield set(splitter_list)


res4, mem_diff4, time_diff4 = splitter('fasl;dfkjasdoij;oierjf;oijf;asdfjqwrqeoqawepokpokpolka;ldfkasdlkf')
print(f'выполнение заняло {mem_diff4} MiB и {time_diff4} секунд')

'''
Вывод:
- вторая реализация функции "splitter_two" расходует меньше память. 
- нет разницы во времени выполнения ( 0.11051 & 0.11028 секунд)
'''
