class Item:
    def __init__(self, next, value):
        self.next = next
        self.value = value

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, item):
        if self.first is None:
            self.first = Item(None, item)
            self.last = self.first
        else:
            n_item = Item(None, item)
            self.last.next = n_item
            self.last = n_item
        self._size += 1
        print('ok')

    def pop(self):
        if self.first is not None:
            item = self.first.value
            self.first = self.first.next
            self._size -= 1
            return item
        else:
            return 'error'

    def front(self):
        if self._size > 0:
            return self.first.value
        else:
            return 'error'

    def size(self):
        return self._size

    def clear(self):
        self.first = None
        self.last = None
        self._size = 0
        print('ok')


queue = Queue()

while True:
    command = input().split()
    if command[0] == 'push':
        queue.push(int(command[1]))
    elif command[0] == 'pop':
        print(queue.pop())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'clear':
        queue.clear()
    elif command[0] == 'exit':
        print('bye')
        raise SystemExit