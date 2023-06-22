"""
Степень четырёх

Напишите программу, которая определяет, будет ли положительное целое число
степенью четвёрки.
Подсказка: степенью четвёрки будут все числа вида 4n,
где n – целое неотрицательное число.

Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.

Формат вывода
Выведите «True», если число является степенью четырёх,
«False» –— в обратном случае.

Пример 1
Ввод	            Вывод
15                  False
"""


x = int(input())


def four(x):
    for i in range(0, 7, 1):
        if x == 4 ** i:
            return True
    return False


if four(x):
    print(True)
else:
    print(False)