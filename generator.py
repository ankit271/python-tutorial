
def square_generator(numbers):    
    for i in numbers:
        yield (i*i)       
    
    
sq_num = square_generator([1,2,3,4,5])

for i in sq_num:
    print(i)

# list comprehensions
squares = (x * x for x in range(5))
for square in squares:
    print(square)
