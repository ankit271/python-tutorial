add = lambda a,b : a+b

print(add(5,6))

numbers = [1, 2, 3, 4]
squared = map(lambda x: x*x, numbers)

print(list(squared))  # Output: [1, 4, 9, 16]
