def binary_search(arr, key, low, high):
    while high > low:
        mid = (low + high) // 2
        print('arr mid = ', arr[mid])
        if arr[mid] == key:
            return f'{key} exists in the array at index {mid}'
        elif key < arr[mid]:
            high = mid
        else:
            low = mid + 1
    return f'{key} doesnt exists in the array'


if __name__ == '__main__':
    arr = [12, 41, 55, 1, 2, 90, 51, 88]
    arr.sort()
    print(arr)
    low, high = 0, len(arr)
    key = 88
    print(binary_search(arr, key, low, high))
