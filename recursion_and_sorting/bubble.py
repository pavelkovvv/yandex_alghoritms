quantity = int(input())
arr = [int(i) for i in input().split()]
steps = len(arr) - 1
arr_prev = arr.copy()
check = 0

for i in range(quantity):
    for j in range(steps):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            check += 1
    if arr != arr_prev:
        print(*arr)
    arr_prev = arr.copy()
    steps -= 1

if check == 0:
    print(*arr)
