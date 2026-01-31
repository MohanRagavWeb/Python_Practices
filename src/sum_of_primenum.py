#18. Find the sum of all prime numbers between 1 and 100.

def is_prime(n):
    if n==1:
        return False

    for i in range(2,n):
        if n%i==0:
            return False
    return True

res=0
for i in range(1,101):
    if is_prime(i):
        res+=i

print(res)