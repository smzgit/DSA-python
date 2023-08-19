def min_del_inst(s1,s2):
    n = len(s1)
    m = len(s2)

    dp = [[-1 for i in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0
    for i in range(m+1):
        dp[0][i] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return n+m - 2*dp[n][m]

if __name__ == '__main__':
    str1 = "heap"
    str2 = "pea"

    ans = min_del_inst(str1,str2)
    print('min deletion & insertion = ',ans)