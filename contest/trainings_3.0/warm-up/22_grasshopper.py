def number_of_ways(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    dp = [0] * n
    dp[0] = dp[1] = 1
    if k >= n:
        k = n-1
    for i in range(2, k + 1):
        for j in range(i-1, -1, -1):
            dp[i] += dp[j]
    for i in range(k+1, n):
        for j in range(i-1, i - k - 1, -1):
            dp[i] += dp[j]
    return dp[n-1]


if __name__ == '__main__':
    N, k = [int(x) for x in input().split()]
    print(number_of_ways(N, k))
