#9.  Create a decorator method `identity_decorator` that transforms `identity(first, middle, last)`
# into a properly cased full name (e.g., `identity("p","eswara","kumar") → "P Eswara Kumar"`).
def identity_decorator(func):
    def wrapper(first, middle, last):
        full_name = f"{first.capitalize()} {middle.capitalize()} {last.capitalize()}"
        return full_name
    return wrapper


@identity_decorator
def identity(first, middle, last):
    return first + " " + middle + " " + last


print(identity("p", "eswara", "kumar"))
