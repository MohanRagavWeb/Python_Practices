#42. Write nested lambdas to perform composed operations.
operation = lambda x: (lambda y: (x + y) * 2)

result = operation(5)(3)
print(result)



operation = lambda a: (lambda b: (a * b) ** 2)

print(operation(2)(3))

