#16. Find the first non-repeating character in a string using loops.
s="abcdabcd"
check=False
for i in s:
    if s.count(i)==1:
        print(i)
        check=True
        break

if check==False:
    print("No non Repeating char in string")