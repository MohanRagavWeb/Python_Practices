# Count the number of digits in an integer without converting it to a string.

n=int(input("Enter a Number: "))
count=0
if n==0:
    count=1
else:
    n=abs(n)
    while n > 0:
        n//=10
        count+=1
print("Number of Digits:",count)
