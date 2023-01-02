# ID 80232162
from math import floor


class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.items.pop()
        else:
            return 'error'

    def plus(self):
        x, y = self.pop(), self.pop()
        self.push(x + y)

    def minus(self):
        x, y = self.pop(), self.pop()
        self.push(y - x)

    def multiply(self):
        x, y = self.pop(), self.pop()
        self.push(x * y)

    def divide(self):
        x, y = self.pop(), self.pop()
        self.push(floor(y / x))


def main():
    expression = input().split()
    stack = Stack()
    operations = {
        '+': stack.plus,
        '-': stack.minus,
        '*': stack.multiply,
        '/': stack.divide,
    }
    for symbol in expression:
        if symbol in operations:
            operations[symbol]()
        else:
            stack.push(int(symbol))
    print(stack.pop())


if __name__ == '__main__':
    main()
