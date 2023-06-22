"""
Соседи
Дана матрица. Нужно написать функцию, которая для элемента возвращает
всех его соседей. Соседним считается элемент, находящийся от текущего
на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы
соседними не считаются.
Например, в матрице A соседними элементами для (0, 0) будут 2 и 0.
А для (2, 1) –— 1, 2, 7, 7.

Формат ввода
В первой строке задано n — количество строк матрицы. Во второй —
количество столбцов m. Числа m и n не превосходят 1000. В следующих n
строках задана матрица. Элементы матрицы — целые числа, по модулю не
превосходящие 1000. В последних двух строках записаны координаты элемента,
соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.

Пример 1
Ввод	            Вывод
4                   7 7
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
"""


n = int(input())
m = int(input())

matrix = [[0 for x in range(m)] for y in range(n)]
z = 0
result = list()

for i in range(n):
    save = list(map(int, input().split()))
    for j in save:
        matrix[i][z] = j
        z += 1
    z = 0

coords_x = int(input())
coords_y = int(input())

if n == 1 and m == 1:
    pass
elif m == 1:
    if coords_x + 1 != n:
        result.append(matrix[coords_x + 1][coords_y])
    if coords_x - 1 != -1:
        result.append(matrix[coords_x - 1][coords_y])
else:
    if coords_x + 1 != n:
        result.append(matrix[coords_x + 1][coords_y])
    if coords_y == 0 or coords_y+1 != m:
        result.append(matrix[coords_x][coords_y+1])
    if coords_y - 1 != -1:
        result.append(matrix[coords_x][coords_y-1])
    if coords_x - 1 != -1:
        result.append(matrix[coords_x-1][coords_y])

result.sort()
for i in result:
    print(i, end=' ')
