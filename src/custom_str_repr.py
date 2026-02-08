#35. Create custom `__str__` and `__repr__` methods in a class.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # for user-friendly output
    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

    # for developer/debug output
    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"


s1 = Student("Mohan", 85)

print(s1)        # calls __str__()
print(repr(s1))  # calls __repr__()
