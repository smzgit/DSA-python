
def dec_bin(n):
    if n==0:
        return 0
    return n%2+10*dec_bin(n//2)

print(dec_bin(2679))