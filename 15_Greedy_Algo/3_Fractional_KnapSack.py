def frac_knap_sack(items: list, capacity: int):
    # add density

    for i in items:
        i.append(i[1] / i[0])

    items.sort(key=lambda x: x[2], reverse=True)
    print(items)
    used_capacity = 0
    tot_val = 0
    for j in items:
        print(j)
        if used_capacity + j[0] <= capacity:
            used_capacity += j[0]
            tot_val+=j[1]
        else:
            wgt_left = capacity-used_capacity
            value = j[2]*wgt_left
            used_capacity+=wgt_left
            tot_val+=value
        if used_capacity==capacity:
            break

    print(f'Total Value obtained = {tot_val} with capacity = {capacity}')


if __name__ == '__main__':
    items = [[20,100],[30,120],[10,60]]
    frac_knap_sack(items,50)
