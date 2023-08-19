#fibonacci recursive/iterative function
import time

def fibonacci(n):
    if n in [0,1]:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n=150
if n>0:
    st1 = time.time()
    print(f'fibo seq of {n} is {fibonacci(n)}')
    print('rec exec time = {}'.format(time.time()-st1))
    st2=time.time()
    a,b=0,1
    for i in range(n):
        g=b
        b=a+b
        a=g

    print(f'fibo seq of {n} is {a}')
    print('itr exec time = {}'.format(time.time() - st2))
else:
    print(f'factorial of {n} doesnt exists!!')