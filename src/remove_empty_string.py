#44. Use `filter()` to remove empty strings from a list.
a = ["Mohan", "", "Ragav"]

def check(x):
    return x != ""   # keep only non-empty strings

b = list(filter(check, a))
print(b)
