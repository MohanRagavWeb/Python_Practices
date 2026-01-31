#15. Find the factorial of a number using a `while` loop.

n=int(input("Enter a number: "))
fact=1
while n>0:
    fact*=n
    n-=1

print("Factorial:",fact)