#26. Write a function to flatten a nested list.

def flatten(nested_list):
    res=[]
    for i in nested_list:
        if type(i)==list:
            for j in i:
                res.append(j)
        else:
            res.append(i)
    return  res
a=[1,2,[1,2],3]
b=flatten(a)
print(b)

