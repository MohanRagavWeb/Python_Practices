#32. Implement encapsulation using private variables.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    # method to deposit money
    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    # method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    # method to view balance
    def get_balance(self):
        return self.__balance


# creating object
b1 = BankAccount("Mohan", 5000)
print("Current Balance:", b1.get_balance())
print(b1.name)
b1.deposit(1000)
b1.withdraw(2000)

# accessing private variable using method
print("Current Balance:", b1.get_balance())

# direct access (not allowed)
# print(b1.__balance)   # will give error
