"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]

from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()

"""
import random
from statistics import median
from timeit import timeit

m = int(input('Введите число: '))
random_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(random_list)


def shell_sort(list_obj):
    last_index = len(list_obj) - 1
    step = len(list_obj) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and list_obj[delta] > list_obj[j]:
                list_obj[delta], list_obj[j] = list_obj[j], list_obj[delta]
                j = delta
                delta = j - step
        step //= 2
    return list_obj


print(shell_sort(random_list))
print(f'Медиана массива: {shell_sort(random_list)[m]}')
print(f'Медиана массива через статистикс: {median(random_list)}')


def median_find(list_obj):
    for i in range(0, len(list_obj) // 2):
        list_obj.remove(max(list_obj))
    return max(list_obj)


print(f'медиана массива без сортировки: {median_find(random_list)}')

print(timeit('shell_sort(random_list[:])[m]', globals=globals(), number=1000))
print(timeit('median(random_list[:])', globals=globals(), number=1000))
print(timeit('median_find(random_list[:])', globals=globals(), number=1000))

'''
Вывод:
- Встроенная функция медианы модуля статистикс оказалась самой быстрой. Превосходит
остальные функции больше чем 13 раз. 

- Поиск медианы через сортировку Шелла на малых m < 50, проигрывает в быстродействии поиску без сортировки. 

- При больших значениях m поиск без сортировки оказывается существенно медленнее Шеллы.
'''