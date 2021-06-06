"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time
def list_add(number):
    time_start = time.time()
    data = [i for i in range(number)]
    time_stop = time.time()
    time_res = time_stop-time_start
    return f'Время на заполнение списка {number} значениями: \n {time_res}'


#
def dict_add(number):
    time_start = time.time()
    data = {a:a for a in range(number)}
    time_stop = time.time()
    time_res = time_stop - time_start
    return f'Время на заполнение словаря {number} значениями: \n {time_res}'


print(list_add(10000))  #  0.000999
print(dict_add(10000))  # 0.001002
print(list_add(1000000))  # 0.076947
print(dict_add(1000000))  #  0.131916
print(list_add(20000000))  # 1.335264
print(dict_add(20000000))  # 1.957784


def list_read(number):
    time_start = time.time()
    data = [i for i in range(number)]
    for i in range(len(data)):
        data.index(i)
    time_stop = time.time()
    time_res = time_stop-time_start
    return f'Время на чтение списка {number} значениями: \n {time_res}'


def dict_read(number):
    time_start = time.time()
    data = {a:a for a in range(number)}
    for i in range(number):
        data.get(i)
    time_stop = time.time()
    time_res = time_stop - time_start
    return f'Время на чтение словаря {number} значениями: \n {time_res}'


print(list_read(10000))  # 0.893448
print(dict_read(10000))  # 0.001996
print(list_read(100000))  # 114.992252
print(dict_read(100000))  # 0.031979
print(list_read(200000))  # 464.786249
print(dict_read(200000))  # 0.063959

"""
После проведения замеров на запись\чтения можно точно сказать, 
что при работе со словарями машина тратит экспонинцеально меньше 
времени в зависимости от количества данных. При записи в списки и 
словари используется константная сложность, а вот при чтении в 
списках используется линейная, в то время как в словарях остаётся константная.
"""
