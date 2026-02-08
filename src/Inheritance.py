#29. Implement inheritance using `Employee` and `Manager` classes.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_employee(self):
        print("Employee name is",self.name)
        print("Salary:",self.salary)

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display_Manager(self):
        print("Manager Dept:",self.department)

m1=Manager("Mohan",30000,"IT")

m1.display_employee()
m1.display_Manager()
