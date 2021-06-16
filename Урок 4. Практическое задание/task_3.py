"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""

import cProfile
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num



cProfile.run('revers(1234512345)')

cProfile.run('revers_2(1234512345)')

cProfile.run('revers_3(1234512345)')

print(timeit("revers(1234512345)", "from __main__ import revers", number=100000))

print(timeit("revers_2(1234512345)", "from __main__ import revers_2", number=100000))

print(timeit("revers_3(1234512345)", "from __main__ import revers_3", number=100000))

"""
После реализации 03 алгоритма сделать выводы :

- через рекурсию - время выполнения 0.2236841 самое затратное 
для данного типа задачи

- через цикл while -  время выполнения 0.15243500000000004 оптимально по решению , 
но при увеличении количества итераций результат будет прибледаться к рекурмивному

- через срез - время выполнения 0.032096299999999967, что является самым быстрым способом 
решения данной задачи. При увеличении количества итераций, время на решение 
остаётся максимально эффективным.
"""
