# ID 79423865
def get_input():
    n = int(input())
    houses = [int(x) for x in input().split()]
    return n, houses


def nearest_zero(n, houses):
    first_zero = 0
    while houses[first_zero] != 0:
        houses[first_zero] = float('inf')
        first_zero += 1
    for i in range(first_zero, n):
        if not houses[i]:
            j = 1
            try:
                while houses[i - j] >= j:
                    houses[i - j] = j
                    j += 1
            except IndexError:
                pass
            k = 1
            try:
                while houses[i + k]:
                    houses[i + k] = k
                    k += 1
            except IndexError:
                pass
    return ' '.join((str(x) for x in houses))


def main():
    print(nearest_zero(*get_input()))


if __name__ == '__main__':
    main()
