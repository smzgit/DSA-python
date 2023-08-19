from collections import Counter as cnt
def longestSubsequenceRepeatedK( s: str, k: int) -> str:
    s_counter = cnt(s)
    print(s_counter)
    def my_lcs(s1,s2):
        n=len(s1)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[0][i] = 0
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(1,n + 1):
            for j in range(1,n + 1):
                if s1[i-1]==s2[j-1] and i!=j and s_counter[s1[i-1]] >= k:
                    dp[i][j] = ord(s1[i-1])+dp[i-1][j-1]
                    s_counter[s1[i - 1]] -=1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        print('LCS LEN = ',dp[n][n])
        for i in range(n + 1):
            for j in range(n + 1):
                print(dp[i][j], ' ', end='')
            print()
        row = n
        col = n
        lcs = ''
        while row > 0 and col > 0:
            if row != col and s1[row - 1] == s2[col - 1]:
                lcs += s1[row - 1]
                row -= 1
                col -= 1
            else:
                if dp[row - 1][col] > dp[row][col - 1]:
                    row -= 1
                else:
                    col -= 1
        return lcs[::-1]

    return my_lcs(s,s)

if __name__ == '__main__':
    s,k="bbabbabbbbabaababab",   3
    ans = longestSubsequenceRepeatedK(s,k)
    print('ans = ',ans)