import math
def get_min_diff(arr):

    actual_sm = sum(arr)
    sm=0
    for i in arr:
        sm += abs(i)
    print('actual_sm = ',actual_sm)
    print('sum = ',sm)
    n=len(arr)

    dp = [[False for _ in range(sm+1)] for _ in range(n+1)]
    for j in range(n+1):
        dp[j][0] = True



    for i in range(1,n+1):
        for j in range(1,sm+1):
            if j>= abs(arr[i-1]):
                dp[i][j] = dp[i-1][j-abs(arr[i-1])] or dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    diff = math.inf
    for k in range((sm//2)+1):
        if dp[n][k]:
            cur_diff = (sm - 2*k)
            diff = abs(min(diff,cur_diff))
    return diff


if __name__ == '__main__':
    nums  = [2]
    ff= get_min_diff(nums)
    print(ff)
