"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(100)]

print(orig_list)
print(bubble_sort(orig_list))

print(timeit.timeit('bubble_sort(orig_list[:])', globals=globals(), number=1000))


def bubble_sort_adjust(lst_obj):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
    return lst_obj


orig_list_adjust = [random.randint(-100, 100) for _ in range(100)]

print(orig_list_adjust)
print(bubble_sort_adjust(orig_list_adjust))


print(timeit.timeit('bubble_sort_adjust(orig_list_adjust[:])', globals=globals(), number=1000))

'''
Вывод: 
- в функции "bubble_sort_adjust" был установлен флаг и она выполняется быстрее примерно 50 раз, чем исходная пузырьковая сортировка "bubble_sort"

'''