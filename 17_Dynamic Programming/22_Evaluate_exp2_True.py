
def get_num_ways(a):
    mapp = dict()
    n=len(a)
    i,j=0,n-1
    def solve(i,j,is_true):
        if i>j:
            return False
        if i==j:
            if is_true:
                return a[i]=='T'
            else:
                return a[i] == 'F'
        kee=str(i)+str(j)+str(is_true)
        if kee in mapp:
            return mapp[kee]
        count = 0

        for k in range(i + 1, j, 2):
            LT = solve( i, k - 1, True)
            LF = solve( i, k - 1, False)
            RT = solve( k + 1, j, True)
            RF = solve( k + 1, j, False)
            if a[k] == '&':
                if is_true:
                    count = count + LT * RT
                else:
                    count = count + LT * RF + LF * RT + LF * RF
            elif a[k] == '|':
                if is_true:
                    count = count + LT * RF + LF * RT + LT * RT
                else:
                    count = count + LF * RF
            elif a[k] == '^':
                if is_true:
                    count = count + LT * RF + LF * RT
                else:
                    count = count + LT * RT + LF * RF
        mapp[kee] = count
        return count

    anss = solve(i,j,True)
    for q,w in mapp.items():
        print(q,' = ',w)
    return anss
if __name__ == '__main__':
    a="T|T&F^T"
    count_ans = get_num_ways(a)
    print(f'number of ways {a} = True are {count_ans}')