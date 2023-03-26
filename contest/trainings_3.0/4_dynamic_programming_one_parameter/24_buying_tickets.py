def min_time_ro_buy(peoples, n):
    if n == 1:
        return peoples[0][0]
    dp = [0] * n
    dp[0] = peoples[0][0]
    if n == 2:
        return min(peoples[0][0] + peoples[1][0], peoples[0][1])
    dp[1] = min(peoples[0][0] + peoples[1][0], peoples[0][1])
    if n == 3:
        min(
            peoples[0][0] + peoples[1][0] + peoples[2][0],
            peoples[0][1] + peoples[2][0],
            peoples[0][0] + peoples[1][1],
            peoples[0][2]
        )
    dp[2] = min(
        peoples[0][0] + peoples[1][0] + peoples[2][0],
        peoples[0][1] + peoples[2][0],
        peoples[0][0] + peoples[1][1],
        peoples[0][2]
    )
    for i in range(3, n):
        dp[i] = min(
            dp[i-1] + peoples[i][0],
            dp[i-2] + peoples[i-1][1],
            dp[i-3] + peoples[i-2][2]
        )
    return dp[n-1]


if __name__ == '__main__':
    n = int(input())
    peoples = []
    for _ in range(n):
        peoples.append([int(x) for x in input().split()])
    print(min_time_ro_buy(peoples, n))
