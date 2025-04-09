def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments passed:", args)
        print("Keyword arguments passed:", kwargs)
        result = func(*args, **kwargs)  # Call the original function
        print("Function executed successfully!")
        return result
    return wrapper


@my_decorator
def greet(name, age=None):
    print(f"Hello, {name}!")
    if age:
        print(f"You are {age} years old.")


# Call the decorated function
greet("Ankit")
