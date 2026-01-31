#2.  Using a decorator, write a code example of your own.

def greeting(func):
    def wrapper():
        print("Hello")
        func()
        print("How Are You?")
    return wrapper
@greeting
def name():
    print("Mohan")

name()
