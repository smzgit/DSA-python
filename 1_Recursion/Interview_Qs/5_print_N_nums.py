def print_nums(n):
    if n<=0:
        return n
    print_nums(n-1)
    print(n)


if __name__ == '__main__':
    n=10
    print_nums(n)