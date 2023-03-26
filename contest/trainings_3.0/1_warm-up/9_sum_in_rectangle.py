if __name__ == '__main__':
    n, m, k = [int(x) for x in input().split()]
    matrix = []
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
        for j in range(m):
            prefix[i + 1][j + 1] = (
                    prefix[i][j + 1] + prefix[i + 1][j] -
                    prefix[i][j] + matrix[i][j]
            )
    for _ in range(k):
        x1, y1, x2, y2 = [int(x) for x in input().split()]
        res = (
                prefix[x2][y2] - prefix[x2][y1 - 1] -
                prefix[x1 - 1][y2] + prefix[x1 - 1][y1 - 1])
        print(res)
