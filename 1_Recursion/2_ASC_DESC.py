
def ascending_seq(n):
    if n<1:
        return n
    ascending_seq(n-1)
    print(n)
def descending_seq(n):
    if n<1:
        return n
    print(n)
    descending_seq(n-1)


print('ASC SEQ')
ascending_seq(10)
print('\n=========================>\n')

print('DESC SEQ')
descending_seq(10)