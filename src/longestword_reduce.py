#46. Find the longest word in a list using `reduce()`.
from functools import reduce
a=["mohan","Ragavendhra","Ragavendhra","Mohan Ragavendhra"]
def check(x,y):
    if len(x)>len(y):
        return x
    else:
        return y

b=reduce(check, a)
print(b)


c=reduce(lambda x,y: x if len(x)>len(y) else y,a)
print(c)