#45. Use `reduce()` to calculate the product of elements in a list.
from functools import reduce
a=[1,2,3,4]
def multi(x,y):
    return x*y
b=reduce(multi,a)
print(b)

c=reduce(lambda x,y: x*y , a)
print(c)