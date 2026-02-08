#49. Combine `map()` and `filter()` in a single program.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# filter even numbers, then square them
result = list(
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, numbers))
)

print(result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def check_even(x):
    return x % 2 == 0

def square(x):
    return x ** 2

result = list(map(square, filter(check_even, numbers)))

print(result)
