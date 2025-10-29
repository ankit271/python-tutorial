
numbers = [1,24,5,6,7,89,9,10,11,12,13,14,15]

def generate_numbers():
    for number in numbers:
        yield number


for num in generate_numbers():
    print(num)
