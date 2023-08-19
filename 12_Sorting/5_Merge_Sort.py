'''
Merge Sort Time and Space Complexity -

1. Space Complexity :- Auxiliary Space: O(n) as Each  recursive call makes a new array

2. Time Complexity :- Merge Sort is a recursive algorithm and time complexity can be expressed
                      as following recurrence relation. T(n) = 2T(n/2) + O(n), The solution of
                      the above recurrence is O(nLogn). The list of size N is divided into a
                      max of Logn parts, and the merging of all sublists into a single list
                      takes O(N) time, the worst-case run time of this algorithm is O(nLogn)
                      Best Case Time Complexity: O(n*log n)
                      Worst Case Time Complexity: O(n*log n)
                      Average Time Complexity: O(n*log n)
                      The time complexity of MergeSort is O(n*Log n) in all the 3 cases (worst,
                      average and best) as the mergesort always divides the array into two
                      halves and takes linear time to merge two halves.
'''
def merge_sort(arr):
    if len(arr) <= 1: # return when arr has only 1 element
        return arr
    mid = len(arr) // 2 # calculate the middle index inorder to split array in left and right sub-arrays 

    left_array = arr[:mid] 
    right_array = arr[mid:]

    # when arrays can't be divided further
    # we can now merge them by comparing their elements
    return merge(merge_sort(left_array), merge_sort(right_array))


def merge(left_array, right_array):
    # left and right pointer are used to compare the values in both
    # subarrays and add them to the result array depending on
    # whichever is smalled
    left_pointer, right_pointer = 0, 0
    result_arr = []

    # now check if any 1 of the subarray has elements
    if left_pointer < len(left_array) or right_pointer < len(right_array):
        # if both of them have elemets just compare each and append it to result array
        while left_pointer < len(left_array) and right_pointer < len(right_array):
            if left_array[left_pointer] < right_array[right_pointer]:
                result_arr.append(left_array[left_pointer])
                left_pointer += 1
            else:
                result_arr.append(right_array[right_pointer])
                right_pointer += 1
        # if some elements are left in left_array just add all of them
        # to the result array
        if left_pointer < len(left_array):
            result_arr.extend(left_array[left_pointer:])
        # if some elements are left in right_array just add all of them
        # to the result array
        if right_pointer < len(right_array):
            result_arr.extend(right_array[right_pointer:])

    return result_arr


if __name__ == '__main__':
    l = [3, 11, 4, 9, 55, 10, 8, 32, 41, 21, 18]
    print(l)
    ans = merge_sort(l)
    print(ans)
