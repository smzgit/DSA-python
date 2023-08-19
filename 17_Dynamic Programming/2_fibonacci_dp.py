def cal_fibo(n):
    '''
    T.C = O(n)
    S.C = O(n)

    :param n:
    :return: fibonacci nth term
    '''
    dp=[-1 for _ in range(n+1)]

    def fibo(num):
        if num==0:
            return 0
        if num==1:
            return 1
        if dp[num]!=-1:
            print('PRESENT !! val = ', dp[num])
            return dp[num]
        else:
            ans1 = fibo(num-1)
            ans2 = fibo(num-2)
            dp[num-1]= ans1
            dp[num-2]= ans2
            return ans1 +ans2
    return fibo(num=n)



from functools import lru_cache
@lru_cache()
def lru_fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return lru_fibo(n-1) + lru_fibo(n-2)
if __name__ == '__main__':
    n=800
    t=cal_fibo(n)
    print('fibo of {} = '.format(n), t)
    print(cal_fibo.__doc__)

    # ans = lru_fibo(n)
    # print('LRU fibo of {} = '.format(n), ans)


