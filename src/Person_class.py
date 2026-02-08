#28. Create a `Person` class with `name` and `age`, and display details.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_details(self):
        print("My Name is",self.name)
        print(f"I'm {self.age} Years Old.")
obj=Person("Mohan",21)
obj.display_details()