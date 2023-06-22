def get_mean(north, south, len_north, len_south):
    length = len_north + len_south
    res_len = length // 2 + 1
    i, j = 0, 0
    res = []
    for k in range(res_len):
        if i < len_north and j < len_south:
            if north[i] < south[j]:
                res.append(north[i])
                i += 1
            else:
                res.append(south[j])
                j += 1
        elif i < len_north:
            res.append(north[i])
            i += 1
        else:
            res.append(south[j])
            j += 1
    return (res[-1] + res[-2]) / 2.0 if (length % 2 == 0) else int(res[-1])


if __name__ == '__main__':
    len_north = int(input())
    len_south = int(input())
    north = [int(i) for i in input().split()]
    south = [int(i) for i in input().split()]
    print(get_mean(north, south, len_north, len_south))
