#22. Create a function that returns both the sum and average of numbers.
def add(a):
    res=0
    for i in a:
        res+=i
    return res
def avg(a):
    res=add(a)
    n=len(a)

    average=res/n
    return average

a=[1,2,3,4,5,6]
addition=add(a)
average=avg(a)
print(addition)
print(average)
