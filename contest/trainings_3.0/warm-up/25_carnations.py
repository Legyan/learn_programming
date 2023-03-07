def thread_length(n, a):
    if n == 2:
        return max(a)
    a.sort()
    dp = [0] * n
    dp[1] = a[1] - a[0]
    dp[2] = a[2] - a[0]
    for i in range(3, n):
        dp[i] = min(dp[i-1], dp[i-2]) + a[i] - a[i-1]
    return dp[-1]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    print(thread_length(n, a))
