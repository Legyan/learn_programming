class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print('ok')

    def pop(self):
        return self.items.pop()

    def back(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        print('ok')


stack = Stack()

while True:
    try:
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            print(stack.pop())
        elif command[0] == 'back':
            print(stack.back())
        elif command[0] == 'size':
            print(stack.size())
        elif command[0] == 'clear':
            stack.clear()
        elif command[0] == 'exit':
            print('bye')
            raise SystemExit
    except IndexError:
        print('error')
