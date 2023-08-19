def findTargetSumWays(nums, target):
    n = len(nums)
    offset = sum(nums)
    if target > offset:
        return 0
    m = offset * 2 + 1
    dp = [[0 for j in range(m)] for i in range(n + 1)]
    dp[0][offset] = 1
    for i in range(1, n + 1):
        for j in range(m):
            if nums[i - 1] <= j:
                dp[i][j] += dp[i - 1][j - nums[i - 1]]
            if j < m - nums[i - 1]:
                dp[i][j] += dp[i - 1][j + nums[i - 1]]
    # print(dp)
    return dp[n][target + offset]

def target_sm(arr, tar) :
    n = len(arr)
    S = 0
    for i in arr:
        S += abs(i)

    if tar > S:
        return 0
    if (tar + S) % 2 != 0:
        return 0
    s1 = (S + abs(tar)) // 2
    dp = [[0 for i in range(s1 + 1)] for i in range(n + 1)]

    for l in range(n + 1):
        dp[l][0] = 1
    for i in range(n + 1):
        for j in range(s1 + 1):
            print(dp[i][j], ' ', end='')
        print()

    print('---------------------------------------')

    for i in range(1, n + 1):
        for j in range(s1 + 1):
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j] # dp[3][3] = dp[2][3-3] + dp[2][3] = 1 + 1 = 2
            elif arr[i - 1] > j or arr[i - 1] == 0:
                dp[i][j] = dp[i - 1][j]

    for i in range(n + 1):
        for j in range(s1 + 1):
            print(dp[i][j], ' ', end='')
        print()
    return dp[n][s1]
if __name__ == '__main__':
    nums = [1,0] # 1+2+1, 1+3, 3+1
    target = 1
    # nums = [100]
    # target = -200
    # ans = findTargetSumWays(nums, target)
    # print('findTargetSumWays => ',ans)
    print('target_sm => ',target_sm(nums,target))
