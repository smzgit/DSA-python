def insertion_sort(a_list):
    for i in range(1,len(a_list)):
        key = a_list[i]
        j=i-1
        while j>=0 and key < a_list[j]:
            a_list[j+1] = a_list[j]
            j -= 1
        a_list[j+1] = key
    return a_list


if __name__ == '__main__':
    l = [3, 11, 4, 9, 55, 10, 8, 32, 41, 21, 18]
    print(insertion_sort(a_list=l))