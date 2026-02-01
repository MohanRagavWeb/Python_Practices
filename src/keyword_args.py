#25. Write a function using keyword arguments (`**kwargs`).
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


student_details(name="Mohan", age=21, department="CSE")
print()
def show_info(**kwargs):
    if 'name' in kwargs:
        print("Name:", kwargs['name'])
    if 'age' in kwargs:
        print("Age:", kwargs['age'])


show_info(name="Mohan", age=21)
