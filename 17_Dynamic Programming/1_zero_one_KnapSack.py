# dp = [[-1]*4]*52
dp = [[-1 for i in range(52)] for j in range(5)]


# exit(1)
def max_value(wgt,vals,C,n):

    if n==0 or C==0:
        return 0
    print('n = ',n)
    print('c = ',C)
    if dp[n-1][C]!=-1:
        print('Present , ans = ',dp[n-1][C])
        return dp[n-1][C]
    if wgt[n-1] <=C:
        ans= max(vals[n-1]+max_value(wgt,vals,C-wgt[n-1],n-1),
                   max_value(wgt,vals,C,n-1))
        dp[n-1][C]=ans
        return ans
    if wgt[n-1]>C:
        ans= max_value(wgt,vals,C,n-1)
        dp[n-1][C]=ans
        return ans


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    ans = max_value(wgt=wt,vals=val,C=W,n=n)
    print('max profit = {}'.format(ans))

