quantity_days = int(input())
arr = [int(i) for i in input().split()]
cost = int(input())


def search_days(arr, cost, left, right):
    if right <= left:
        if right == left == 0:
            return 1
        return -1
    mid = (left + right) // 2
    if arr[mid] >= cost > arr[mid - 1]:
        return mid + 1
    elif cost <= arr[mid]:
        return search_days(arr, cost, left, mid)
    else:
        return search_days(arr, cost, mid+1, right)


print(search_days(arr, cost, 0, quantity_days), end=' ')
print(search_days(arr, cost*2, 0, quantity_days), end=' ')
