#ID 81277542
from random import randint


class Participant:
    __slots__ = ['name', 'tasks', 'fine']
    def __init__(self, name, tasks, fine):
        self.name = name
        self.tasks = tasks
        self.fine = fine

    def __gt__(self, other):
        if self.tasks != other.tasks:
            return self.tasks > other.tasks
        if self.fine != other.fine:
            return self.fine < other.fine
        return self.name < other.name

    def __lt__(self, other):
        if self.tasks != other.tasks:
            return self.tasks < other.tasks
        if self.fine != other.fine:
            return self.fine > other.fine
        return self.name > other.name

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __str__(self):
        return self.name


def get_input():
    n = int(input())
    if not 1 <= n <= 100000:
        raise ValueError(
            'The number of participant must be '
            'in the range from 1 to 100_000'
        )
    table = []
    for i in range(n):
        name, tasks, fine = input().split()

        if len(name) > 20:
            raise ValueError(
                'String length must be no more '
                'than 20 characters'
            )
        if not 0 <= int(tasks) <= 10 ** 9 or \
                not 0 <= int(fine) <= 10 ** 9:
            raise ValueError(
                'The number of solved problems and fine must be '
                'in the range from 0 to 1_000_000_000'
            )
        table.append(Participant(name, int(tasks), int(fine)))
    return table


def quicksort(table, start, end):
    if end - start >= 1:
        pivot_index = randint(start, end)
        table[start], table[pivot_index] = table[pivot_index], table[start]
        pivot = table[start]
        left = start + 1
        right = end
        while True:
            while left <= right and table[left] >= pivot:
                left += 1
            while left <= right and table[right] <= pivot:
                right -= 1
            if left <= right:
                table[left], table[right] = table[right], table[left]
            else:
                table[start], table[right] = table[right], table[start]
                break
        quicksort(table, start, right)
        quicksort(table, right + 1, end)

def main():
    table = get_input()
    quicksort(table, 0, len(table) - 1)
    print(*table, sep='\n')

if __name__ == '__main__':
    main()
