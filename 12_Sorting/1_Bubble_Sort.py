def bubble_sort(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list)-i-1):
            if a_list[j]>a_list[j+1]:
                print('swapping =>',a_list[j],' & ',a_list[j+1])
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]
    return a_list


if __name__ == '__main__':
    # l=[3,11,4,9,55,10,8,32,41,21,18]
    l=[5, 1, 4, 2, 8]
    print(bubble_sort(l))
