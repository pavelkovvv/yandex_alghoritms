# ID успешной посылки: 86827948
class DequeIsEmptyError(Exception):
    pass


class DequeIsFullError(Exception):
    pass


class Deque:
    def __init__(self, n):
        self._queue = [None] * n
        self._max_n = n
        self._head = 0
        self._tail = 0
        self._size = 0

    def _is_empty(self):
        return self._size == 0

    def _is_full(self):
        return self._size == self._max_n

    def _new_index(self, attr_name: str, plus_or_minus: bool):
        attr_value = getattr(self, attr_name)
        new_value = ((attr_value + 1) % self._max_n if plus_or_minus else
                     (attr_value - 1) % self._max_n)
        setattr(self, attr_name, new_value)

    def push_back(self, value):
        if self._is_full():
            raise DequeIsFullError('Deque is full, cannot add element.')
        self._queue[self._tail] = value
        self._new_index('_tail', True)
        self._size += 1

    def pop_front(self):
        if self._is_empty():
            raise DequeIsEmptyError('Deque is empty, cannot extract element.')
        x = self._queue[self._head]
        self._queue[self._head] = None
        self._new_index('_head', True)
        self._size -= 1
        return x

    def pop_back(self):
        if self._is_empty():
            raise DequeIsEmptyError('Deque is empty, cannot extract element.')
        x = self._queue[self._tail - 1]
        self._queue[self._tail - 1] = None
        self._new_index('_tail', False)
        self._size -= 1
        return x

    def push_front(self, value):
        if self._is_full():
            raise DequeIsFullError('Deque is full, cannot add element.')
        self._new_index('_head', False)
        self._size += 1
        self._queue[self._head] = value


def main():
    quantity = int(input())
    max_n = int(input())
    x = Deque(max_n)
    for i in range(quantity):
        command, *value = input().split()
        try:
            if len(value) > 0:
                value = value[0]
                getattr(x, command)(int(value))
            else:
                print(getattr(x, command)())
        except (DequeIsEmptyError, DequeIsFullError):
            print('error')


if __name__ == '__main__':
    main()
