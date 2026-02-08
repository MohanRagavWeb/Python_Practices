#38. Demonstrate the `else` block in exception handling.
try:
    a = int(input("Enter a number: "))
    b = 10 / a

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    print("Division successful")
    print("Result:", b)
