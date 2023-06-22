class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class StackMax:
    def __init__(self):
        self.head = None
        self.tail = None
        self.max_stack = []

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.max_stack.append(value)
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            max_value = max(self.max_stack[-1], value)
            self.max_stack.append(max_value)

    def pop(self):
        if self.head is None:
            print('error')
        else:
            self.max_stack.pop()
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def get_max(self):
        if self.head is None:
            print(None)
        else:
            print(self.max_stack[-1])


quantity = int(input())
val = StackMax()
for i in range(quantity):
    x = [j for j in input().split()]
    if x[0] == 'get_max':
        val.get_max()
    elif x[0] == 'pop':
        val.pop()
    elif x[0] == 'push':
        val.push(value=int(x[1]))
