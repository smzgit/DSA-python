#reotate a square matrix by 90 degree

def rotate90Clockwise(A):
    n = len(A[0])
    l,r = 0,n-1

    while l<r:
        for i in range(r-l):
            top,bottom=l,r
            tmp = A[top][l+i]
            A[top][l+i]=A[bottom-i][l]
            A[bottom-i][l]=A[bottom][r-i]
            A[bottom][r-i]=A[top+i][r]
            A[top+i][r]=tmp
        l+=1
        r-=1



def onn_liner(A):
    return list(zip(*A[::-1]))

# Function to print the matrix
def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        print(A[i])


# Driver code
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16],]

B  = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16],]
rotate90Clockwise(A)
printMatrix(A)
print(onn_liner(B))
#output -
# [13, 9, 5, 1]
# [14, 10, 6, 2]
# [15, 11, 7, 3]
# [16, 12, 8, 4]