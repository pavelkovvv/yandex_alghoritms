# ID успешной посылки: 86821452
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def main():
    arr = input().split()
    x = Stack()
    symbol_operation = {
        '+': lambda v1, v2: v2 + v1,
        '-': lambda v1, v2: v2 - v1,
        '/': lambda v1, v2: v2 // v1,
        '*': lambda v1, v2: v2 * v1
    }
    for elem in arr:
        if elem in symbol_operation:
            el1 = x.pop()
            el2 = x.pop()
            res = symbol_operation[elem](el1, el2)
            x.push(res)
        else:
            elem = int(elem)
            x.push(elem)
    print(x.pop())


if __name__ == '__main__':
    main()
