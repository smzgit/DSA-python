def get_max_amount(nums,n,dp):
    if n<=0:
        return 0
    else:
        dp[n] = max(nums[n-1]+get_max_amount(nums,n-2,dp),get_max_amount(nums,n-1,dp))

    return dp[n]


def max_amount(nums,n):
    dp = [0 for i in range(n+1)]

    for i in range(2,n+1):
        dp[i] = max(nums[i-2]+dp[i-2],dp[i-2])
    print(dp)
    return dp[n]



if __name__ == '__main__':
    nums = [2,7,9,3,1]
    n=len(nums)
    dp = [-1 for _ in range(n+1)]
    ans =get_max_amount(nums,n,dp)
    print(ans)
    print('===============================')
    print(max_amount(nums,n))
