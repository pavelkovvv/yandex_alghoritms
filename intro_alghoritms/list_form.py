"""
Списочная форма

Вася просил Аллу помочь решить задачу. На этот раз по информатике.
Для неотрицательного целого числа X списочная форма –— это массив его
цифр слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1].
На вход подается количество цифр числа Х, списочная форма неотрицательного
числа Х и неотрицательное число K. Числа К и Х не превосходят 10000.

Нужно вернуть списочную форму числа X + K.

Формат ввода
В первой строке — длина списочной формы числа X. На следующей строке —
сама списочная форма с цифрами записанными через пробел.
В последней строке записано число K, 0 ≤ K ≤ 10000.

Формат вывода
Выведите списочную форму числа X+K.

Пример 1
Ввод	            Вывод
4                   1 2 3 4
1 2 0 0
34
"""


q = int(input())
arr = list(map(str, input().split()))
k = int(input())

x = "".join(arr)
x = int(x)
sum_ = x + k
sum_ = str(sum_)

for i in sum_:
    print(i, end=' ')
