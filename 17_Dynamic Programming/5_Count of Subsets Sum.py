def get_count_subset(arr,k,n):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1


    for i in range(1,n+1):
        for j in range(1,k+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][k]

if __name__ == '__main__':
    arr =[3, 5, 6, 7,2,1,8]
    X = 9
    n = len(arr)
    cnt = get_count_subset(arr,X,n)
    print('SUBSET COUNT = {}'.format(cnt))

    print('----------------------------------------------------')


