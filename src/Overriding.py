#30. Demonstrate method overriding with a real-world example.

class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} is a animal")
class Dog(Animal):
    def __init__(self,name,dogname):
        super().__init__(name)
        self.dogname=dogname
    def sound(self):
        print(f"{self.dogname} is a {self.name} and makes bow bow sound")

d1=Dog("Dog","Jimmy")
d1.sound()

