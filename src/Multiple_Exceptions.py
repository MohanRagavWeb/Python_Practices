#36. Catch multiple exceptions in a single `try` block.
try:
    a = int(input("Enter a number: "))
    b = 10 / a
    print("Result:", b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input! Enter a number")

"""
try:
    a = int(input("Enter a number: "))
    b = 10 / a
    print("Result:", b)

except (ZeroDivisionError, ValueError) as e:
    print("Error occurred:", e)

"""