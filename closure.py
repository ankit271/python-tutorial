
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()  # Call the original function
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")


def say_goodbye():
    print("Goodbye, World!")
# Call the decorated function
# func = my_decorator(say_hello)
# func()
say_hello()
say_goodbye()


# def outer_func(message):
#     def inner_func():
#         print(message)
#     return inner_func


# inner = outer_func("Hi")

# inner()