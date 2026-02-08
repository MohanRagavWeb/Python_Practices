#27. Write a function that returns another function (closure).

"""
A closure is a function that
remembers the variables from its outer function even
after the outer function has finished executing.
"""
def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function

result=outer_function(25)
final=result(100)
print(final)