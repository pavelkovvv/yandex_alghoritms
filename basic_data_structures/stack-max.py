class StackMax:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_max(self):
        print(max(self.items))


n = int(input())
cl = StackMax()
for i in range(n):
    x = [j for j in input().split()]
    try:
        if x[0] == 'get_max':
            cl.get_max()
    except ValueError:
        print(None)
    try:
        if x[0] == 'pop':
            cl.pop()
    except IndexError:
        print('error')
    if x[0] == 'push':
        cl.push(int(x[1]))
