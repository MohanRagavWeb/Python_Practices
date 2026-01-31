#17. Print a pyramid pattern of `*` using nested loops.
n = 4
for i in range(n):

    # spaces
    for j in range(n-i-1):
        print(" ", end="")

    # stars
    for k in range(2*i+1):
        print("*", end="")

    print()

# n=4
# for i in range(n):
#     print(" "*(n-i-1)+"*"*(2*i+1))