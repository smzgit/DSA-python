'''
for any given positive number , return the
sum of it's digits using recursion
'''

def sum_digits(n):
    if n<10:
        return n
    return n%10+sum_digits(n//10)

n=13211232314121
print(sum_digits(n))


#iterative method
ans=0
while n>0:
    ans+=n%10
    n//=10
print(ans)