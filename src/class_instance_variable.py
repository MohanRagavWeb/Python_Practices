#31. Create a class variable and an instance variable—show the difference.
class Student:
    college = "ACE Engineering College"   # class variable

    def __init__(self, name, marks):
        self.name = name        # instance variable
        self.marks = marks      # instance variable



s1 = Student("Mohan", 85)
s2 = Student("Rahul", 90)


print("Student 1:", s1.name, s1.marks, s1.college)
print("Student 2:", s2.name, s2.marks, s2.college)
