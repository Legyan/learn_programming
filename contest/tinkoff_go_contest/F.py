def main():
    n, x = [int(i) for i in input().split()]
    points = [int(i) for i in input().split()]
    cristals = 0
    days = 0
    while True:
        i = 0
        while True:
            days += 1
            tmp = cristals + points[i]
            if tmp == x:
                return days
            elif tmp > x and tmp - points[0] > x:
                break
            elif tmp > x and not tmp - points[0] > x:
                return -1
            cristals = tmp
            if i < n - 1:
                i += 1


if __name__ == '__main__':
    print(main())
