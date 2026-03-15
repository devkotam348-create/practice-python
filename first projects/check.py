def my_decorator(func):
    def inner():
        print("Before function")
        func()
        print("After function")
    return inner

@my_decorator
def greet():
    print("Hello")

x = greet
print(x())
