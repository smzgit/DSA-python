
def canPartition(nums):
    K = sum(nums)
    if K%2!= 0:
        return False
    else:
        K//=2

    n=len(nums)
    dp=[[False for _ in range(K+1)] for _ in range(n+1)]

    for i in range(K+1):
        dp[0][i]=False
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,K+1):
            if j>= nums[i-1]:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] =dp[i - 1][j]

    return dp[n][K]


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    ans = canPartition(nums)
    print(nums, 'can be equally sum partitioned??  = ',ans)
    nums = [4, 4]
    ans = canPartition(nums)
    print(nums, 'can be equally sum partitioned??  = ',ans)
