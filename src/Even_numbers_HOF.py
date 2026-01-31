#3.  Select even numbers from a list using higher-order functions (`map`, `filter`).
a=[1,2,3,4,5,6]
b=list(filter(lambda x: x%2==0,a))
print(b)

def even(x):
    return x%2==0
c=list(filter(even,a))
print(c)

a = [1, 2, 3, 4, 5, 6]
b = list(filter(None, map(lambda x: x if x % 2 == 0 else None, a)))
print(b)
