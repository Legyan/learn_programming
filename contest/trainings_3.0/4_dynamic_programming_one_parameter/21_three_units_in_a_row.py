def number_of_sequences(n):
    match n:
        case 0:
            return 0
        case 1:
            return 2
        case 2:
            return 4
        case 3:
            return 7
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 2, 4, 7
    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3])
    return dp[n]


if __name__ == '__main__':
    N = int(input())
    print(number_of_sequences(N))
