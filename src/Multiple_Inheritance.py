#34. Implement multiple inheritance with a simple example.
# Parent class 1
class Father:
    def skills_father(self):
        print("Father: Gardening skills")


# Parent class 2
class Mother:
    def skills_mother(self):
        print("Mother: Cooking skills")


# Child class inheriting from both parents
class Child(Father, Mother):
    def skills_child(self):
        print("Child: Coding skills")


# creating object
c1 = Child()

# accessing all methods
c1.skills_father()
c1.skills_mother()
c1.skills_child()
