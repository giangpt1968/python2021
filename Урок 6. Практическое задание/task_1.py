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
def min_value(lst):
    min_v = lst[0]
    for i in lst:
        if i < min_v:
            min_v = i
    return min_v


res, mem_diff, time_diff = min_value(list(range(1000000)))
print(f'выполнение заняло {mem_diff} MiB и {time_diff} секунд')


@decor
def min_value_two(lst):
    min_v = lst[0]
    for i in lst:
        if i < min_v:
            min_v = i
            yield min_v


res2, mem_diff2, time_diff2 = min_value(list(range(1000000)))
print(f'выполнение заняло {mem_diff2} MiB и {time_diff2} секунд')

'''
Вывод:
- вторая реализация функции методом "ленивых вычичслений" с помощью генератора
расходует меньше память. 
- нет большой  разницы во времени выполнения ( 0.12789899999999998 & 0.1408686 секунд)
'''