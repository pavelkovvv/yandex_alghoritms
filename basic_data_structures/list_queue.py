# Реализация класса (единичного объекта двусвязного списка)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


# Реализация очереди на двусвязном списке
class ListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def put(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def get(self):
        if self.head is None:
            print('error')
        else:
            self.size -= 1
            if self.head == self.tail:
                print(self.head.value)
                self.head = None
                self.tail = None
            else:
                x = self.head
                self.head = self.head.next
                self.head.prev = None
                x.next = None
                print(x.value)

    def sized(self):
        print(self.size)


quantity = int(input())
val = ListQueue()

for i in range(quantity):
    x = [j for j in input().split()]
    if x[0] == 'put':
        val.put(int(x[1]))
    elif x[0] == 'get':
        val.get()
    elif x[0] == 'size':
        val.sized()
