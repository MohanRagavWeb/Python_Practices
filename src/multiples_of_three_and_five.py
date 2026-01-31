#13. Print numbers 1–100; for multiples of 3 print `"Three"`, for 5 print `"Five"`, and for both print `"ThreeFive"`.


for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("ThreeFive")

    elif i % 3 == 0:
        print("Three")

    elif i % 5 == 0:
        print("Five")

    else:
        print(i)
