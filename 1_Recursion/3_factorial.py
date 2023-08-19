#factorial recursive/iterative function
import time

def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

n=9
if n>0:
    st1 = time.time()
    print(f'factorial of {n} is {factorial(n)}')
    print('rec exec time = {}'.format(time.time()-st1))
    st2=time.time()
    ans=n
    while (n>1):
        n -= 1
        ans*=n

    print(ans)
    print('itr exec time = {}'.format(time.time() - st2))
else:
    print(f'factorial of {n} doesnt exists!!')