#10. Write code for the Fibonacci series.

def fibo(n):
    if n==1 or n==0:
        return n
    return fibo(n-2)+fibo(n-1)

n=7

for i in range(n):
    print(fibo(i), end=" ")
print("\n")
print(fibo(n))

print("\n")
###using generators

def fibo_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibo_generator(7):
    print(num, end=" ")

