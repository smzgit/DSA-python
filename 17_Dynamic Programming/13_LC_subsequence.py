'''
LC - 1143 - https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.
 If there is no common subsequence, return 0.

'''


# def longestCommonSubsequence(text1, text2):
#     n = len(text1)
#     m = len(text2)
#     print('n = ',n)
#     print('m = ',m)
#
#
#
#     dp = [[-1 for i in range(m + 1)] for i in range(n + 1)]
#
#     def find_ans(s1, n, s2, m):
#         if n == 0 or m == 0:
#             return 0
#         # if dp[n][m] != -1:
#         #     return dp[n][m]
#         if s1[n - 1] == s2[m - 1]:
#             # dp[n - 1][m - 1] = 1 + find_ans(s1, n - 1, s2, m - 1)
#             return 1 + find_ans(s1, n - 1, s2, m - 1)#dp[n - 1][m - 1]
#
#         else:
#             # dp[n][m] =  return max(dp[n][m - 1], dp[n - 1][m])
#             return dp[n][m] #max(find_ans(s1, n, s2, m - 1),find_ans(s1, n - 1, s2, m))
#
#     return find_ans(text1, n, text2, m)
#     for i in range(n + 1):
#         for j in range(m + 1):
#             print(dp[i][j], ' ', end='')
#         print()
#     return dp[n-1][m-1]


def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)
    print('N = ',n,' & M = ',m)
    d=''

    dp = [[-1 for i in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                d+=text1[i-1]
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], ' ', end='')
        print()
    print('LCS = ',d)
    return dp[n][m]




if __name__ == '__main__':
    # text1 = "abcde"
    #
    # text2 = "ace"
    text1 ="AGGTAB"
    text2 = "GXTXAYB"

    lcs = longestCommonSubsequence(text1, text2)
    print('ANS = ', lcs)
    print('\n\n--------------------------------------')
    s = "bbbab"
    lcs = longestCommonSubsequence(s,s[::-1])