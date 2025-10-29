
num1 = {1,2,3,4,5}

num2 = {6,7,8,9,10, 5}

print(num1 | num2)
print(num1.union(num2))

print(num1.intersection(num2))

print(num1.difference(num2))

num1.update(num2)

print(num1)