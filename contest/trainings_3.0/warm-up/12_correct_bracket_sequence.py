class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


parentheses = input()


def parentheses_valid(parentheses):
    stack = Stack()
    dict_of_parentheses = {')': '(', ']': '[', '}': '{'}
    try:
        for i in range(len(parentheses)):
            if parentheses[i] in dict_of_parentheses.values():
                stack.push(parentheses[i])
            else:
                if stack.items[-1] == dict_of_parentheses[parentheses[i]]:
                    stack.pop()
                else:
                    return False
    except Exception:
        return False
    return len(stack.items) == 0


if parentheses_valid(parentheses):
    print('yes')
else:
    print('no')
