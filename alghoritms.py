quantity = int(input())
climbers = []
step = quantity - 1
mem_del = 0

for i in range(quantity):
    in_ = [int(i) for i in input().split()]
    climbers.append(in_)

print(climbers)j

for i in range(quantity):
    for j in range(step):
        if climbers[j][0] == climbers[j+1][0] and climbers[j][1] == climbers[j+1][1]:
            mem = climbers[len(climbers)-1]
            climbers[j], climbers[len(climbers)-1] = climbers[len(climbers)-1], climbers[j]
            mem_del += 1
        elif climbers[j][0] < climbers[j+1][0] and climbers[j][1] > climbers[j+1][1]:
            climbers[j+1], climbers[len(climbers)-1-mem_del] = climbers[len(climbers)-1-mem_del], climbers[j+1]
            mem_del += 1
        elif climbers[j][0] > climbers[j+1][0] and climbers[j][1] < climbers[j+1][1]:
            climbers[j], climbers[len(climbers)-1-mem_del] = climbers[len(climbers)-1-mem_del], climbers[j]
            mem_del += 1

for i in range(mem_del):
    climbers.pop()
print(climbers)
