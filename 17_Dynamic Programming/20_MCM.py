# Input: arr[] = {40, 20, 30, 10, 30}
# Output: 26000

def min_matrix_cost(arr,i,j):
    if i>=j:
        return 0
    ans=float('inf')
    for k in range(i,j) :
        temp_ans = min_matrix_cost(arr,i,k) + min_matrix_cost(arr,k+1,j) + arr[i-1]*arr[k]*arr[j]
        ans=min(ans,temp_ans)

    return ans

def memoized_method(arr):
    n=len(arr)
    dp = [[-1 for i in range(n+1)]for _ in range(n+1)]


    i,j=1,n-1
    def min_matrix_cost2(arr,i,j):

        if i>=j:
            return 0
        if dp[i][j]!=-1:
            print('matched !!')
            return dp[i][j]

        ans = float('inf')
        for k in range(i,j) :
            temp_ans = min_matrix_cost2(arr,i,k) + min_matrix_cost2(arr,k+1,j) + arr[i-1]*arr[k]*arr[j]
            ans=min(ans,temp_ans)

        dp[i][j]=ans

        return ans
    return min_matrix_cost2(arr,i,j)


if __name__ == '__main__':
    arr = [40, 20, 30, 10, 30]
    ans = min_matrix_cost(arr,1,len(arr)-1)
    print(f'1 - Min cost of multiplication = {ans}')

    ans = memoized_method(arr)
    print(f'2 - Min cost of multiplication = {ans}')