'''
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
'''
def ways(coins,amount,n) :
    dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
    for k in range(n+1) :
        dp[k][0] = 1

    for i in range(n+1):
        for j in range(amount+1) :
            print(dp[i][j],' ',end='')
        print()

    for i in range(1,n+1):
        for j in range(1,amount+1) :
            if coins[i-1] <= j:
                dp[i][j] =dp[i][j-coins[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    print('\nno of ways =>')
    print(dp[n][amount])

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    #
    # amount = 10
    # coins = [10]
    #
    # amount = 10
    # coins = [2, 5, 3, 6]

    ways(coins,amount,len(coins))
