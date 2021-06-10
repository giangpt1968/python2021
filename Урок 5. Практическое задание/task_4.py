"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
import random
simple_dict = {}
some_orderedDict = OrderedDict()


def simple_dict_add():
    for i in range(10000):
        simple_dict[i] = random.random()
    return simple_dict


def some_orderedDict_add():
    for i in range(10000):
        some_orderedDict[i] = random.random()
    return some_orderedDict


def dict_popitem():
    simple_dict.popitem()
    return simple_dict


def ordereddict_popitem():
    some_orderedDict.popitem()
    return some_orderedDict


print(timeit('simple_dict_add()', globals=globals(), number=2000))
print(timeit('some_orderedDict_add()', globals=globals(), number=2000), end='\n\n')

print(timeit('dict_popitem()', globals=globals(), number=10000))
print(timeit('ordereddict_popitem()', globals=globals(), number=10000), end='\n\n')

print(timeit('reversed(simple_dict)', globals=globals(), number=10000))
print(timeit('reversed(some_orderedDict)', globals=globals(), number=10000), end='\n\n')

print(timeit('simple_dict.clear()', globals=globals(), number=10000))
print(timeit('some_orderedDict.clear()', globals=globals(), number=10000), end='\n\n')
'''
- Во всех замерах операции с обычным словарем срабатывают немного быстрее чем операции с упорядоченным
словарем из модуля коллекций. 

- Может и есть специфические ситуации, где исользование OrderedDict будет предпочтительнее,
OrderedDict в Python 3.6 и более поздних версиях
'''