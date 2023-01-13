def moving_average(n, mass, k):
    res = []
    summ = 0
    for i in range(k):
        summ += mass[i]
    res.append(summ/k)
    for j in range(k, n):
        summ -= mass[j-k]
        summ += mass[j]
        res.append(summ/k)
    return ' '.join(map(str, res))


if __name__ == '__main__':
    n = int(input())
    mass = list(map(int, input().split()))
    k = int(input())
    print(moving_average(n, mass, k))
