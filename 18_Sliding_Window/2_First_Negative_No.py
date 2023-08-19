def first_neg_num(arr, k):
    ans=[]
    f,l=-1,len(arr)
    for i in range(k):
        if arr[i]<0 and f==-1:
            ans.append(arr[i])
            f=i


    for j in range(k,len(arr)):
        if f>=j-k:
            ans.append(arr[f])
        if arr[j]<0 and l-f>k:
            l=j

        if f<j-k:
            f=l

    return ans





if __name__ == '__main__':
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    print(first_neg_num(arr,k))