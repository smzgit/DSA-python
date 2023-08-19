'''
https://leetcode.com/problems/shortest-common-supersequence/

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
 If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number
 of characters from t (possibly 0) results in the string s
'''


def super_seq(s1,s2):

    n=len(s1)
    m=len(s2)
    dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(m+1):
        dp[0][i] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] =max(dp[i][j-1],dp[i-1][j])

    lcs = ''
    row=n
    col=m
    while row > 0 and col > 0:
        if s1[row - 1] == s2[col - 1]:
            lcs += s2[col - 1]
            row -= 1
            col -= 1
        else:
            if dp[row - 1][col] > dp[row][col - 1]:
                row -= 1
            else:
                col -= 1
    lcs =  lcs[::-1]
    print('longest common substring = ', lcs)

    ans=''

    s1_ptr, s2_ptr = 0,0
    for i in range(len(lcs)):
        while (s1_ptr < len(s1) and s1[s1_ptr] != lcs[i]) :
            ans+=s1[s1_ptr]
            s1_ptr+=1
            print('ans after adding s1 non-lcs => ',ans)
        print()
        while (s2_ptr < len(s2) and s2[s2_ptr] != lcs[i]) :
            ans+=s2[s2_ptr]
            s2_ptr+=1
            print('ans after adding s2 non-lcs => ', ans)


        # if s1[s1_ptr]==lcs[i] and s2[s2_ptr]==lcs[i]:
        ans+=lcs[i]
        s1_ptr+=1
        s2_ptr+=1

        print('ans after  adding lcs => ', ans)
        print()
        print()
        print()


    while s1_ptr < len(s1) :
        ans += s1[s1_ptr]
        s1_ptr += 1
    while s2_ptr < len(s2):
        ans += s2[s2_ptr]
        s2_ptr += 1
    return ans


if __name__ == '__main__':
    str1 = "abac"
    str2 = "cab"

    ans = super_seq(str1,str2)
    print(ans,'\n\n\n\n')
    s="leetcode"
    print(super_seq(s,s[::-1]))