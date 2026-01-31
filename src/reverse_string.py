#8.  Reverse a string without using built-in reverse functions.
s="Mohan"
rev=""
for i in s:
    rev=i+rev
print(rev)
print(s[::-1])