
def diag_sum(A):
    n=len(A)
    sm=0
    for i in range(n):
        sm+=A[i][i]
        sm += A[i][n - i - 1]

    return sm

# Driver code
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(diag_sum(A))