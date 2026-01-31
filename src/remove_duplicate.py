#19. Iterate over a list and remove duplicate elements without using `set`.
a=[1,2,3,1,2,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)

print(b)