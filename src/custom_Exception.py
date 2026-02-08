#37. Write a custom exception for invalid age input.
# creating custom exception
class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Valid age")


try:
    age = int(input("Enter age: "))
    check_age(age)

except InvalidAgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Please enter a valid number")
