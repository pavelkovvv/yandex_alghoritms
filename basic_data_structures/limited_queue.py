# Реализация ограниченной очереди
class MyQueueSized:
    def __init__(self, max_sized: int):
        self.queue = [None] * max_sized
        self.max_n = max_sized
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def sized(self):
        return self.size

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

quantity_command = int(input())
max_sized = int(input())
x = MyQueueSized(max_sized)

for i in range(quantity_command):
    # Список для записи и обработки введённых пользователем комманд
    list_command = [i for i in input().split()]
    if list_command[0] == 'push':
        x.push(list_command[1])
    elif list_command[0] == 'pop':
        print(x.pop())
    elif list_command[0] == 'size':
        print(x.sized())
    elif list_command[0] == 'peek':
        print(x.peek())
