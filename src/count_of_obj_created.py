#33. Write a class that tracks the number of objects created.
class Student:
    count = 0   # class variable to track objects

    def __init__(self, name):
        self.name = name
        Student.count += 1



s1 = Student("Mohan")
s2 = Student("Rahul")
s3 = Student("Anu")
s4 = Student("Vijay")

print("Total objects created:", Student.count)
