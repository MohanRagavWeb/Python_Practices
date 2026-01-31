#For input `s = "aabbbffff"`, output character counts like `a = 2 times`, `b = 3 times`, etc.
s="aabbbffff"
a=[]

for i in s:
    if i not in a:
        print(f"{i} = {s.count(i)} times", end=", ")
        a.append(i)