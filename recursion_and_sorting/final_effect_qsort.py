# ID успешной посылки: 87972678
class Participant:
    def __init__(self, name, points, penalty):
        self.name = name
        self.points = points
        self.penalty = penalty

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, Participant):
            return (
                    (-self.points, self.penalty, self.name) <
                    (-other.points, other.penalty, other.name)
            )
        return NotImplemented


def quicksort(arr: list, start=0, end=0):
    def partition(low, high):
        if low >= high:
            return None
        left = low
        right = high
        pivot = arr[(right + left) // 2]
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        partition(low, right)
        partition(left, high)
    partition(start, end - 1)


if __name__ == '__main__':
    quantity = int(input())
    participants = []
    for index in range(quantity):
        name, points, penalty = input().split()
        participants.append(
            Participant(points=int(points), penalty=int(penalty), name=name)
        )
    quicksort(participants, end=len(participants))
    print(*participants, sep='\n')
