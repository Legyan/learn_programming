class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def nearest_smaller_to_the_right(N, cities):
    stack = Stack()
    results = [-1] * N
    for i in range(N):
        while stack.size() and stack.peek()[0] > cities[i]:
            tmp = stack.pop()
            results[tmp[1]] = i
        stack.push((cities[i], i))
    return ' '.join(str(result) for result in results)


if __name__ == '__main__':
    N = int(input())
    cities = list(map(int, input().split()))
    print(nearest_smaller_to_the_right(N, cities))
