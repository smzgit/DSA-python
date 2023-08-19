'''
https://www.geeksforgeeks.org/longest-common-substring-dp-29/

Given two strings text1 and text2, return the length of their longest common Substring.
 If there is no common Substring, return 0.

'''

ans = 0


def solve(i, j, s1, s2, n, m, dp):
    global ans

    # i is the starting index for s1
    # j is the starting index for s2

    if (i >= n or j >= m):
        return 0

    if (dp[i][j] != -1):
        return dp[i][j]

    if (s1[i] == s2[j]):
        dp[i][j] = 1 + solve(i + 1, j + 1, s1, s2, n, m, dp)

    else:
        dp[i][j] = 0

    solve(i, j + 1, s1, s2, n, m, dp)
    solve(i + 1, j, s1, s2, n, m, dp)
    ans = max(ans, dp[i][j])  # ans is storing maximum till now

    return dp[i][j]


def rec_LCS(s1,s2):
    n=len(s1)
    m=len(s2)


    dp = [[-1 for i in range(m + 1)] for i in range(n + 1)]

    s_len = 0

    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 0#max(dp[i - 1][j], dp[i][j - 1])
            s_len = max(s_len,dp[i][j])

    # for i in range(n + 1):
    #     for j in range(m + 1):
    #         s_len = max(dp[i][j],s_len)

    return s_len
if __name__ == '__main__':
    text1 = "abc"
    text2 = "bcc"

    # global ans
    # n is the length of s1
    # m is the length s2
    dp = [[-1 for i in range(len(text2))] for j in range(len(text1))]
    ans = 0
    solve(0, 0, text1, text2, len(text1),len(text2), dp)
    # return ans
    print('ANS (memoization) = ', ans)
    lcs2 = rec_LCS(text1, text2)
    print('ANS (tabular) = ', lcs2)
