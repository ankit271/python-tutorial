
# def logger(original_function):    
#     def wrapper_function(*args):
#         print(original_function.__name__)
#         print(args)
#         return original_function(*args)
#     return wrapper_function



# @logger
# def sayHi(name):
#     print("Welcome to {}".format(name))
    
# sayHi("Python")

def logger(fucn):
    def wapper_function(*args):
        print("hii")
        return fucn(args[0], args[1])  # 30
    return wapper_function

@logger
def multiply(a,b):    
    return a*b;

data = multiply(5,6)
print(data)
