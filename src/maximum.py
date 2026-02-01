#21. Write a function to return the maximum element from a list.
def maximum(a):
    maxi=a[0]

    for i in a:
        if i>maxi:
            maxi=i
    return maxi
a=[1,2,3,14,5]
res=maximum(a)
print(res)
