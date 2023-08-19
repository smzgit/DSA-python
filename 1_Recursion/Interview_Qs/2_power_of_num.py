def power_num(n,p):
    if p==0:
        return 1
    return n*power_num(n,p-1)

n=2
p=3
print(power_num(n,p))