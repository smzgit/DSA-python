def printLCS(s1,s2) :
    n=len(s1)
    m=len(s2)

    dp = [[-1 for _ in range(m+1)] for _ in range(n+1) ]

    for i in range(n+1):
        dp[i][0] = 0
    for i in range(m+1):
        dp[0][i] = 0
    s_len = 0
    row = n
    col = m
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 0
            # s_len = max(s_len, dp[i][j])
            if dp[i][j] > s_len:
                row = i
                col = j
                s_len= dp[i][j]

    lcs =''
    print('row = ',row)
    print('col = ',col)
    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], ' ', end='')
        print()
    while row > 0 and col > 0:
        if s1[row-1] == s2[col-1]:
            lcs+=s2[col-1]
            row-=1
            col-=1
        else:
            if dp[row-1][col] > dp[row][col-1] :
                row-=1
            else:
                col-=1
    print('longest common substring = ',lcs[::-1])
    return s_len


if __name__ == '__main__':
    text1 = "abcdxyz"
    text2 = "xyzabcd"

    lcs2 = printLCS(text1, text2)
    print('ANS (tabular) = ', lcs2)
    #
    #
    # #
    # open_chars = ['(', '[', '{']
    # closed_reversed = {
    #     ')': '(',
    #     ']': '[',
    #     '}': '{'
    # }
    #
    # stack = []
    # for ch in line:
    #     if ch in open_chars:
    #         stack.append(ch)
    #     elif len(stack) < 1 or stack.pop() != closed_reversed[ch]:
    #         return False
    #
    # return len(stack) == 0
