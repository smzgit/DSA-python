from functools import lru_cache


def minCut(s) :
    n=len(s)
    if n<=1:
        return 0
    dp = [[-1 for i in range(n + 1)] for _ in range(n + 1)]

    @lru_cache(None)
    def is_palindrome(i,j):
        if i>=j:
            return True
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def solve(i,j) :
        if i>=j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if is_palindrome(i,j):
            return 0

        ans=float('inf')
        for k in range(i,j):
            tempans = dp[i][k] if dp[i][k]!=-1 else solve(i,k)
            tempans += dp[k+1][j] if dp[k+1][j]!=-1 else solve(k+1,j)

            tempans +=1
            ans=min(ans,tempans)
        dp[i][j]=ans
        return ans
    return solve(0,n-1)

if __name__ == '__main__':
    '''
    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return the minimum cuts needed for a palindrome partitioning of s.
    '''
    s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
    ans =minCut(s)
    print(f'Min partitions = {ans}')
