# Unbounded- knapsack
def max_profit2(prices,len_arr,rod_len):

    dp =[[0 for i in range(rod_len+1)] for j in range(rod_len+1)] #[[0 for _ in range(rod_len+1)] for _ in range(prices+1) ]


    for i in range(1,rod_len+1) :
        for j in range(1,rod_len+1) :
            if len_arr[i-1] <= j:
                dp[i][j] = max(prices[i-1] + dp[i][j-len_arr[i-1]],  dp[i-1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[rod_len][rod_len]
if __name__ == '__main__':
   prices = [1, 5, 8, 9, 10, 17, 17, 20]
    # prices = [3  , 5 ,  8  , 9,  10  ,17  ,17  ,20]
    # len_arr = [i for i in range(1,len(prices)+1)]
    # rod_len = len(prices)
    # print(len_arr)
    #
    # print('MAX PROFIT =>',max_profit2(prices,len_arr,rod_len))
