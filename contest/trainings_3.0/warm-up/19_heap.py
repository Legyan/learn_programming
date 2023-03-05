class Heap:
    def __init__(self):
        self.items = []

    def insert(self, k):
        self.items.append(k)
        self.sift_up(len(self.items) - 1)

    def extract(self):
        if len(self.items) == 1:
            return self.items.pop()
        max_val = self.items[0]
        self.items[0] = self.items.pop()
        self.sift_down(0)
        return max_val

    def sift_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.items[i] > self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            self.sift_up(parent)

    def sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.items) and self.items[left] > self.items[largest]:
            largest = left
        if right < len(self.items) and self.items[right] > self.items[largest]:
            largest = right
        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            self.sift_down(largest)


if __name__ == '__main__':
    n = int(input())
    heap = Heap()
    for i in range(n):
        cmd = input().split()
        if cmd[0] == '0':
            heap.insert(int(cmd[1]))
        else:
            print(heap.extract())
