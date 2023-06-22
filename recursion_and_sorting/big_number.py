quantity = int(input())
arr = input().split()
steps = len(arr) - 1

for i in range(quantity):
    for j in range(steps):
        if int((arr[j] + arr[j+1])) < int((arr[j+1] + arr[j])):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("".join(arr))
