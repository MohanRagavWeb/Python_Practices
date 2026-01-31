#1.  Use reduce to sum the elements of a list.
from functools import reduce
a=[1,2,3,4,5]
def add(a,b):
    return a+b

b=reduce(add,a)
# USING_LAMBDA c=reduce(lambda a,b: a+b,a)
print(b)
