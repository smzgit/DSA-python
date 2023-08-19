def select_activity(activity):
    a = sorted(activity, key=lambda x: x[2])
    for i in a:
        print(i)
    cnt = 0
    end = None
    for j in a:
        if not end:
            end = j[2]
            print(j[0] + ' -> ', end='')
            cnt += 1
        elif end <= j[1]:
            cnt += 1
            print(j[0] + ' -> ', end='')
            end = j[2]

    print()
    return cnt


if __name__ == '__main__':
    activity = [
        ['A1', 0, 6],
        ['A2', 3, 4],
        ['A3', 1, 2],
        ['A4', 5, 8],
        ['A5', 5, 7],
        ['A6', 8, 9],
    ]

    ans = select_activity(activity)
    print('Max activities performed = ', ans)
