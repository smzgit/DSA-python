def max_sum_subarray(arr,k):
    n=len(arr)
    sm=0
    ans=float('-inf')
    for j in range(k):
        sm+=arr[j]
    for i in range(k,n):
        sm += arr[i]-arr[i-k]
        ans=max(ans,sm)
    return ans

if __name__ == '__main__':
    arr = [100, 200, 300, 400]
    k = 2
    print(max_sum_subarray(arr,k))