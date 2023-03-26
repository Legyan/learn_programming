from collections import deque


def drunk_game(first, second):
    max_count = 10 ** 6
    for i in range(1, max_count):
        f, s = first.popleft(), second.popleft()
        if f > s and not (f == 9 and s == 0) or (f == 0 and s == 9):
            first.append(f)
            first.append(s)
        else:
            second.append(f)
            second.append(s)
        if not first:
            return 'second', i
        elif not second:
            return 'first', i
    return 'botva'


if __name__ == '__main__':
    first_player = deque([int(x) for x in input().split()])
    second_player = deque([int(x) for x in input().split()])
    print(*drunk_game(first_player, second_player))
