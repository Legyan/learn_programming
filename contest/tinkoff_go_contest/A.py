def main():
    n, m = [int(num) for num in input().split()]
    minibus = [False] * m
    for passenger in range(n):

        if m % 2 != 0:
            mid = m // 2
            i = 0
            try:
                while True:
                    if not minibus[mid - i]:
                        minibus[mid - i] = True
                        print(mid - i + 1)
                        i += 1
                        break
                    elif not minibus[mid + i]:
                        minibus[mid + i] = True
                        print(mid + i + 1)
                        i += 1
                        break
                    i += 1
            except IndexError:
                minibus = [None] * m
                minibus[mid] = True
                print(mid + 1)
        else:
            mid = m // 2 - 1
            i = 0
            try:
                while True:
                    if not minibus[mid - i]:
                        minibus[mid - i] = True
                        print(mid - i + 1)
                        break
                    elif not minibus[mid + i + 1]:
                        minibus[mid + i + 1] = True
                        print(mid + i + 2)
                        break
                    i += 1
            except IndexError:
                minibus = [None] * m
                minibus[mid] = True
                print(mid + 1)


if __name__ == '__main__':
    main()
