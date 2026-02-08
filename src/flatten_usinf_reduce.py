#50. Use `reduce()` to flatten a list of lists.
from functools import reduce

a = [[1, 2], [3, 4], [5, 6]]

def flatten(x, y):
    return x + y

result = reduce(flatten, a)
print(result)


a = [[1, 2], [3, 4], [5, 6]]

result = reduce(lambda x, y: x + y, a)
print(result)