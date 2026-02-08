#40. Sort a list of tuples using a lambda key function.
data = [("Mohan", 90), ("Rahul", 85), ("Anu", 100)]

# sort based on marks
data.sort(key=lambda x: x[1])
# data.sort(key=lambda x: x[0])
print(data)
