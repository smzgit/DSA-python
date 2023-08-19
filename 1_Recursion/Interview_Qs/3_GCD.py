'''
Euclidean Algorithm-

Pseudo Code of the Algorithm-
Step 1:  Let  a, b  be the two numbers
Step 2:  a mod b = R
Step 3:  Let  a = b  and  b = R
Step 4:  Repeat Steps 2 and 3 until  a mod b  is greater than 0
Step 5:  GCD = b
Step 6: Finish
'''
def gcd(a,b):

    r=a%b
    if r==0:
        return b
    return gcd(b,r)


a=516
b=1220

ans=gcd(a,b)
print(ans)