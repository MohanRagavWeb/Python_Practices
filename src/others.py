"""
frequency without count()
"""
a=[1,2,3,4,2,4]
b=[]
for i in a:
    if i not in b:
        c=0
        for j in a:
            if i==j:
                c+=1
        b.append(i)
        print(f"{i} = {c} times",end=", ")


