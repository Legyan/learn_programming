def main():
    n, m = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]

    def fine(speechs):
        fine = 0
        for i in range(speechs):
            fine += i
        return fine

    if sum(p) < m:
        print(-1)
    else:
        for i in range(n):
            if sum(p) - fine(n // (i + 1)) >= m:
                print(i + 1)
                break


if __name__ == '__main__':
    main()
