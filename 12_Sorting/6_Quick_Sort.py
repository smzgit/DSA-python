def quic_sort(arr,left,right):
    if left<right:
        pivot_index = partition_position(arr,left,right)
        quic_sort(arr,left,pivot_index-1)
        quic_sort(arr,pivot_index+1,right)
    return arr

def partition_position(arr,left,right):
    i=left
    j=right-1
    pivot_element = arr[right]
    while i<j:
        while i < right and arr[i] < pivot_element:
            i+=1
        while j > left and arr[j] >= pivot_element:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot_element:
        arr[i], arr[right] = arr[right], arr[i]
    return i

if __name__ == '__main__':
    rr=[5,4,3,2,1]
    print(quic_sort(rr,0,len(rr)-1))
