"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

# Это реализация задачи 6

class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


if __name__ == '__main__':
    qc_obj = QueueClass()
    qc_rev_obj = QueueClass()
    qc_close_obj = QueueClass()

    """
    Проверка. Очередь пустая
    """
    print(qc_obj.is_empty())

    """
    помещаем объекты в очередь
    """

    qc_obj.to_queue(1)
    qc_obj.to_queue(2)
    qc_obj.to_queue(3)
    qc_obj.to_queue(4)
    qc_obj.to_queue(5)
    qc_obj.to_queue(6)
    qc_obj.to_queue(7)
    qc_obj.to_queue(8)
    qc_obj.to_queue(9)

"""
Функция условия разбора очереди. 
"""


def job_qc_obj(list_obj):
    for i in range(list_obj.size()):
        if qc_obj.elems[list_obj.size() - 1] % 3 == 0:
            qc_close_obj.to_queue(list_obj.from_queue())
        else:
            qc_rev_obj.to_queue(list_obj.from_queue())


"""
Условие запуска
"""
if not qc_obj.is_empty():
    job_qc_obj(qc_obj)

"""
Вывод для проверки
"""
print(qc_obj.elems)  # Задачa на выполненa
print(qc_rev_obj.elems)  # Задачи на доработке
print(qc_close_obj.elems)  # Закрытые задачи

