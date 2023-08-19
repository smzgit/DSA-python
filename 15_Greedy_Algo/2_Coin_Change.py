def coin_change(denominations:set,amount:int)->int:
    coins = 0
    while amount!=0:
        if len(denominations)>0:
            max_coin = max(denominations)

        if amount >= max_coin:
            print('Amount = ', amount, '      max amount = ', max_coin)
            amount-=max_coin
            coins += 1

        if amount < max_coin:
            denominations.remove(max_coin)


    return coins


if __name__ == '__main__':
    # coins = {1,2,5,10,20,50,100,1000}
    coins = {1,2,5,20,50,100}
    # summ = 201
    summ = 2035
    min_coins = coin_change(denominations=coins,amount=summ)
    print(f'Minimum number of coins for amount {summ} required are {min_coins}')
