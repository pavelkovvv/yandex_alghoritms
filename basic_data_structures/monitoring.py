n = int(input())  # Число строк
m = int(input())  # Число столбцов

arr = list() # Список для хранения значений

# Считываем данные ввода
for i in range(n):
    arr.append([i for i in input().split()])

# Выводим данные на экран
for i in range(m):
    for j in range(n):
        print(arr[j][i], end=' ')
    print(' ')
