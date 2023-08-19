'''
You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

def get_min_coins(coins,amount,n):
    dp=[[-1 for _ in range(amount+1)] for _ in range(n+1)]

    for i in range(1,amount+1):
        dp[0][i] = float('inf')
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1,amount+1):
        if i % coins[0]==0:
            dp[1][i] = i // coins[0]
        else:
            dp[1][i] = float('inf')

    for i in range(2,n+1):
        for j in range(1,amount+1) :
            if j >= coins[i-1]:
                dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    if dp[n][amount]== float('inf'):
       return -1
    return dp[n][amount]
if __name__ == '__main__':
    # coins = [1, 2, 5]
    # amount = 11
    coins =[2, 5, 10, 1]
    amount = 27
    n=len(coins)
    ans = get_min_coins(coins,amount,n)
    print('MIN COINS REQ. => ',ans)
