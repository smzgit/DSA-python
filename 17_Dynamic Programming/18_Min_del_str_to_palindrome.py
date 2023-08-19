def minimum_deletion(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(m + 1):
        dp[0][i] = 0
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    row = n
    col = m
    lcs = ''
    while row > 0 and col > 0:
        if s1[row-1] == s2[col-1]:
            lcs+=s1[row-1]
            row-=1
            col-=1
        else:
            if dp[row-1][col] > dp[row][col-1]:
                row-=1
            else:
                col-=1
    print('LCS = ',lcs[::-1])


    return abs(dp[n][m] - n)


if __name__ == '__main__':
    s = 'mbadm'
    ans = minimum_deletion("lets","leetcode")
    print('Min deletions = {}'.format(ans))

    '''
    also check min. number of insertions to make palindrome (lcs or prob 16 can solve this)
    https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
    '''
