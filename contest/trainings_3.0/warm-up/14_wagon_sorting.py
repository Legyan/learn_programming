class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def back(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

n = int(input())
wagons = [int(x) for x in input().split()]
stack = Stack()
last = 0
for wagon in wagons:
    stack.push(wagon)
    while stack.size() != 0 and stack.back() == last + 1:
        stack.pop()
        last += 1

if stack.size() != 0:
    print('NO')
else:
    print('YES')
