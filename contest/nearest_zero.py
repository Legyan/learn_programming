# ID 79393277
def main():
    n = int(input())
    houses = [int(x) for x in input().split()]

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

    print(' '.join((str(x) for x in houses)))

if __name__ == '__main__':
    main()
