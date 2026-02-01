#20. Given a list, rotate it `k` times using loops.
#left
a = [1, 2, 3, 4]
k = 2

n = len(a)

for _ in range(k):
    first = a[0]
    for i in range(n - 1):
        a[i] = a[i + 1]
    a[n - 1] = first

print(a)

#right
a = [1, 2, 3, 4]
k = 2

n = len(a)

for _ in range(k):
    last = a[-1]
    for i in range(n - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = last

print(a)

#without loop (-k for right)
# a=[1,2,3,4,5]
# k=2
# k=k%len(a)
# b=[]
#
# b=a[k:]+a[:k]
# print(b)
