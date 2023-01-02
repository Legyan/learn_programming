class Deck:
    def __init__(self, n):
        self.max_n = n
        self.items = [None] * n
        self.size = 0
        self.head = 0
        self.tail = 0

    def push_back(self, value):
        if self.size != self.max_n:
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            if self.size == 0:
                self.head = self.head - 1 if self.head != 0 else self.max_n - 1
            self.size += 1
        else:
            print('error')

    def push_front(self, value):
        if self.size != self.max_n:
            self.items[self.head] = value
            self.head = self.head - 1 if self.head != 0 else self.max_n - 1
            if self.size == 0:
                self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop_back(self):
        if self.size != 0:
            self.tail = self.tail - 1 if self.tail != 0 else self.max_n - 1
            x = self.items[self.tail]
            self.items[self.tail] = None
            self.size -= 1
            if self.size == 0:
                self.head = self.tail
            return x
        else:
            return 'error'

    def pop_front(self):
        if self.size != 0:
            self.head = (self.head + 1) % self.max_n
            x = self.items[self.head]
            self.items[self.head] = None
            self.size -= 1
            if self.size == 0:
                self.tail = self.head
            return x
        else:
            return 'error'


def main():
    commands = int(input())
    max_items = int(input())
    deck = Deck(max_items)
    methods = {
        'push_back': deck.push_back,
        'push_front': deck.push_front,
        'pop_back': deck.pop_back,
        'pop_front': deck.pop_front,
    }
    for i in range(commands):
        command = input().split()
        if command[0][:4] == 'push':
            methods[command[0]](command[1])
        else:
            print(methods[command[0]]())


if __name__ == '__main__':
    main()
