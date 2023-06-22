def counting_(array):
    counts = [0] * 3
    counts[0] = array.count(0)
    counts[1] = array.count(1)
    counts[2] = array.count(2)
    sorted_array = []
    for i, count in enumerate(counts):
        sorted_array.extend([i] * count)
    return sorted_array

if __name__ == '__main__':
    _ = int(input())
    array = [int(num) for num in input().split()]
    sorted_array = counting_(array)
    print(*sorted_array)
