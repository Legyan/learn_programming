from math import floor
import re


class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()


def get_expression():
    expression = input().split()
    for symbol in expression:
        try:
            number = int(symbol)
            if abs(number) > 10000:
                raise ValueError(
                    'Numbers must not exceeding 10000 in absolute value'
                )
        except ValueError:
            if not re.fullmatch(r'[+-/*]{1}', symbol):
                raise ValueError(
                    'Symbol must be integer number or arithmetic symbol'
                )
    return expression


def main():
    expression = get_expression()
    stack = Stack()
    OPERATIONS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: floor(y / x),
    }
    for symbol in expression:
        if symbol in OPERATIONS:
            x, y = stack.pop(), stack.pop()
            stack.push(OPERATIONS[symbol](x, y))
        else:
            stack.push(int(symbol))
    print(stack.pop())


if __name__ == '__main__':
    main()
