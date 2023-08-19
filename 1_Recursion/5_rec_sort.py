def add_ele(arr, last_ele):
    print(f'2. arr = {arr}')
    if len(arr)==0:
        arr.append(last_ele)
        return
    if arr[-1]<=last_ele:
        arr.append(last_ele)
        return

    end_ele = arr[-1]
    arr.pop()
    add_ele(arr,last_ele)
    arr.append(end_ele)


def recursive_sort(arr):
    print(f'1. arr = {arr}')
    if len(arr)<=1:
        return

    last_ele=arr[-1]
    arr.pop()
    recursive_sort(arr)
    add_ele(arr,last_ele)
    return arr


if __name__ == '__main__':
    arr=[5,4,3,2,1]
    ans=recursive_sort(arr)
    print(ans)