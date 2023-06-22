# ID успешной посылки: 86275918
def main():
    quantity = int(input())
    arr = [int(x) for x in input().split()]
    def distance(x: str):
        right_or_left = None
        dist = [quantity] * quantity
        last_zero = -1
        if x == 'right':
            right_or_left = enumerate(arr)
        elif x == 'left':
            right_or_left = reversed(list(enumerate(arr)))
        for index, value in right_or_left:
            if value == 0:
                last_zero = index
                dist[index] = 0
            if last_zero != -1:
                if x == 'right':
                    dist[index] = index - last_zero
                elif x == 'left':
                    dist[index] = last_zero - index
        return dist

    dist_ = [min(r, l) for r, l in zip(distance('right'), distance('left'))]
    print(*dist_)


if __name__ == '__main__':
    main()
