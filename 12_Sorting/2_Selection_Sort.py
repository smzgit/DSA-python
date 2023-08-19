def selection_sort(a_list):
    for i in range(len(a_list)):
        ind = i
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[ind]:
                ind = j
        a_list[i], a_list[ind] = a_list[ind], a_list[i]
    return a_list


if __name__ == '__main__':
    l = [3, 11, 4, 9, 55, 10, 8, 32, 41, 21, 18]
    print(selection_sort(l))
