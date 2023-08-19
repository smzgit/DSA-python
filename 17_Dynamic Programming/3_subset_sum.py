'''
Given a list of integers S and a target number k, write a function that returns a subset of S
that adds up to k. If such a subset cannot be made, then return null.Integers can appear more
than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''


# def subsetsum(arr, n, target):
#     dp = [[False for i in range(target + 1)] for j in range(n + 1)]
#     for i in range(n + 1):
#         dp[i][0] = True
#
#     for i in range(1, target + 1):
#         dp[0][i] = False
#     for i in range(1, n + 1):
#         for j in range(1, target + 1):
#             if j < arr[i - 1]:
#                 dp[i][j] = dp[i - 1][j]
#             if j >= arr[i - 1]:
#                 dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - arr[i - 1]])
#     return dp[n][target]

def sum_possible(arr, n, sm):
    dp = [[False for _ in range(sm + 1)] for _ in range(n + 1)]
    for i in range(sm + 1):
        dp[0][i] = False
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    cb=0
    for i in range(n + 1):
        for j in range(sm + 1):
            print(dp[i][j],' ',end='')
        print()
    print('CB = {}'.format(cb))
    return dp[n][sm]


def recur_subset(arr, K, n):
    if K == 0 and n == 0:
        return True

    if n != 0 and K == 0:  #
        return True

    if n == 0 and K != 0:  #
        return False

    elif arr[n - 1] <= K:
        return (recur_subset(arr, K - arr[n - 1], n - 1) or recur_subset(arr, K, n - 1))
    else:
        return recur_subset(arr, K, n - 1)


if __name__ == '__main__':
    ans = False
    S = [12, 1, 61, 5, 9, 2]
    k = 24
    n = len(S)
    ans = sum_possible(arr=S, n=n, sm=k)
    if ans:
        print('Sum is possible')
    else:
        print('Sum is not possible')

    print('-------------------------------------------')
    nums = [3, 5, 6, 7]
    target = 9
    sz=len(nums)
    print(recur_subset(arr=nums, K=target, n=sz))
    #
    #
    #
    # if (subsetsum(S, n, k) == True):
    #     print('Sum is possible')
    # else:
    #     print('Sum is not possible')
