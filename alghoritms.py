# ID успешной посылки: 87949388
import locale


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivt = arr[high][1]
    i = low - 1
    for j in range(low, high):
        if (arr[j][1] > pivt or (arr[j][1] == pivt and arr[j][2]
                                 < arr[high][2]) or
                (arr[j][1] == pivt and arr[j][2] == arr[high][2]
                 and locale.strcoll(arr[j][0], arr[high][0]) < 0)):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


quantity = int(input())
arr = [5] * quantity

for i in range(quantity):
    x, y, z = input().split()
    arr[i] = [str(x), int(y), int(z)]

quicksort(arr, 0, len(arr)-1)

for i in range(quantity):
    print(arr[i][0])
