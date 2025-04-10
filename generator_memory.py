
def square_generator(numbers):
    for i in numbers:
        yield (i*i)


sq_num = square_generator([1, 2, 3, 4, 5])




