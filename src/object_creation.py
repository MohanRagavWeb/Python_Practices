#5.  Create a class and demonstrate creating an object of that class.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_name(self):
        return self.name
    def display_age(self):
        print(self.age)

obj=person("Mohan",21)
name=obj.display_name()
print(name)
obj.display_age()