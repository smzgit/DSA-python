def get_count(arr, n, diff):
    sm = sum(arr)
    K = (sm + diff) // 2
    print(K)

    dp = [[0 for _ in range(K + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, K + 1):
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    for i in range(n + 1):
        for j in range(K + 1):
            print(dp[i][j], '  ', end='')
        print()
    return dp[n][K]


if __name__ == '__main__':
    N = 5
    D = 1
    ARR = [1, 2, 3, 1, 2]

    cnt = get_count(ARR, N, D)
    print('COUNT = ', cnt)
