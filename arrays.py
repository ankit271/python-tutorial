import array as arr

numbers = arr.array('i', [1, 2, 3,2, 4,2, 5])  # 'i' indicates the type of elements (integer)

# numbers.append(6)  # Append a new element
# numbers.remove(2)  # Output: array('i', [1, 2, 3, 4, 5])
# numbers.extend([7, 8, 9])  # Extend the array with new elements
# print(numbers)

for number in numbers:
    print(number)  # Output: 1 2 3 2 4 2 5