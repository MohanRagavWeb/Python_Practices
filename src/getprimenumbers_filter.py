#48. Use `filter()` to get prime numbers from a list.

a=[1,2,3,4,5,6,7,8,9,10]
def check(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

b=list(filter(check,a))
print(b)



primes = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, x)), a))

print(primes)
