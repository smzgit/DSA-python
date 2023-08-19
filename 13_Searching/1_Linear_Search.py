def linear_search(arr,key):
    # also called as sequential search
    for i in arr:
        if i==key:
            return f'{key} exists in the array at index {arr.index(i)}'
    return f'{key} doesnt exists in the array'


if __name__ == '__main__':
    arr=[12,41,55,1,2,90,51,88]
    print(arr)
    print(linear_search(arr,51))
