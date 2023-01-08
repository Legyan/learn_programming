# ID 80418066
class Deck:
    def __init__(self, n):
        self.max_n = n
        self.items = [None] * n
        self.size = 0
        self.head = 0
        self.tail = 0

    def push_back(self, value):
        if self.size == self.max_n:
            raise IndexError('The deck is full')
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        if self.size == 0:
            self.head = self.head - 1 if self.head != 0 else self.max_n - 1
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_n:
            raise IndexError('The deck is full')
        self.items[self.head] = value
        self.head = self.head - 1 if self.head != 0 else self.max_n - 1
        if self.size == 0:
            self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError('The deck is empty')
        self.tail = self.tail - 1 if self.tail != 0 else self.max_n - 1
        x = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
        if self.size == 0:
            self.head = self.tail
        return x

    def pop_front(self):
        if self.size == 0:
            raise IndexError('The deck is empty')
        self.head = (self.head + 1) % self.max_n
        x = self.items[self.head]
        self.items[self.head] = None
        self.size -= 1
        if self.size == 0:
            self.tail = self.head
        return x


def get_input():
    try:
        commands = int(input())
        if commands > 100000 or commands <= 0:
            raise ValueError(
                'The number of commands must be '
                'in the range from 0 to 100000')
        max_items = int(input())
        if max_items > 50000 or max_items <= 0:
            raise ValueError(
                'Size of deck must be '
                'in the range from 0 to 50000')
        return commands, max_items
    except ValueError:
        ValueError(
            'The number of commands and size of the deck must be '
            'a number')


def main():
    commands, max_items = get_input()
    deck = Deck(max_items)
    METHODS = {
        'push_back': deck.push_back,
        'push_front': deck.push_front,
        'pop_back': deck.pop_back,
        'pop_front': deck.pop_front,
    }
    for i in range(commands):
        command = input().split()
        try:
            if command[0][:4] == 'push':
                METHODS[command[0]](command[1])
            else:
                print(METHODS[command[0]]())
        except IndexError:
            print('error')


if __name__ == '__main__':
    main()
