def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)


if __name__ == '__main__':
    # 0 1 1 2 3 5 8 13 21 34
    term  = 8
    for i in range(term):
        print(fibo(i),' ', end='')
