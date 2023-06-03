quantity = int(input())
arr = [int(i) for i in input().split()]

counter = 0
add_arr = [0, 0, 0]
res_arr = []

for i in arr:
    add_arr[i] += 1


for i in add_arr:
    for j in range(i):
        res_arr.append(counter)
    counter += 1

print(*res_arr)
