# ID 81412478
from dataclasses import dataclass
from typing import List


@dataclass(order=True, frozen=True)
class Participant:
    """Участник соревнования"""
    tasks: int
    fine: int
    name: str

    def __str__(self):
        return self.name


def get_input() -> List[Participant]:
    """Получение и валидация входных данных"""
    try:
        n = int(input())
    except ValueError:
        raise ValueError(
            'The number of participant must be integer'
        )
    if not 1 <= n <= 100_000:
        raise ValueError(
            'The number of participant must be '
            'in the range from 1 to 100_000'
        )
    table = [None] * n
    try:
        for i in range(n):
            name, tasks, fine = input().split()
            tasks = int(tasks)
            fine = int(fine)
            if len(name) > 20:
                raise ValueError(
                    'String length must be no more '
                    'than 20 characters'
                )
            if (not 0 <= tasks <= 1_000_000_000 or
                    not 0 <= fine <= 1_000_000_000):
                raise ValueError(
                    'The number of solved problems and fine must be '
                    'in the range from 0 to 1_000_000_000'
                )
            table[i] = Participant(-tasks, fine, name)
    except ValueError:
        raise ValueError(
            'The number of tasks and fines must be integer'
        )
    return table


def quicksort(table: List[Participant], start: int, end: int) -> None:
    """Быстрая сортировка списка на месте"""
    if end - start >= 1:
        pivot_index = start
        table[start], table[pivot_index] = table[pivot_index], table[start]
        pivot = table[start]
        left = start + 1
        right = end
        while True:
            while left <= right and table[left] <= pivot:
                left += 1
            while left <= right and table[right] >= pivot:
                right -= 1
            if left <= right:
                table[left], table[right] = table[right], table[left]
            else:
                table[start], table[right] = table[right], table[start]
                break
        quicksort(table, start, right)
        quicksort(table, right + 1, end)


def main() -> None:
    table = get_input()
    quicksort(table, 0, len(table) - 1)
    print(*table, sep='\n')


if __name__ == '__main__':
    main()
