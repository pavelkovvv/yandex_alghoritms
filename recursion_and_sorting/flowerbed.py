quantity = int(input())
climbers = []

for i in range(quantity):
    in_ = [int(i) for i in input().split()]
    climbers.append(in_)

merged_climbers = []
climbers = sorted(climbers, key=lambda x: x[0])

for i in climbers:
    if len(merged_climbers) == 0:
        merged_climbers.append(i)
    elif merged_climbers[-1][0] < i[0] and merged_climbers[-1][1] == i[0]:
        merged_climbers[-1][1] = i[1]
    elif merged_climbers[-1][0] < i[0] and merged_climbers[-1][1] > i[0] and i[1] > merged_climbers[-1][0] and i[1] > merged_climbers[-1][1]:
        merged_climbers[-1][1] = i[1]
    elif merged_climbers[-1][0] == i[0] and merged_climbers[-1][1] == i[1]:
        continue
    elif i[0] > merged_climbers[-1][0] and i[1]> merged_climbers[-1][1]:
        merged_climbers.append(i)
    elif merged_climbers[-1][0] < i[0] and merged_climbers[-1][1] > i[1]:
        continue

for i in merged_climbers:
    print(*i)
