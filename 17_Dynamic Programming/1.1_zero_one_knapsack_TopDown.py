
def max_value(wgt, vals, C, n):
    dp = [[-1 for i in range(C + 1)] for j in range(n + 1)]
    for i in range(C + 1):
        dp[0][i] = 0
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            if (wgt[i - 1] <= j):
                dp[i][j] = max(vals[i - 1] + dp[i - 1][j - wgt[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][C]


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    ans = max_value(wgt=wt, vals=val, C=W, n=n)
    print('max profit = {}'.format(ans))
