#47. Use `map()` with multiple iterables.
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x +y, a, b))
print(result)

def add(x, y):
    return x + y

a = [10, 20, 30]
b = [1, 2, 3]

result = list(map(add, a, b))
print(result)
