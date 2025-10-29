import copy
items = ["cherry", "apple", "banana" ]


new_items = copy.deepcopy(items)
items[1] = "orange"


print(items)
print(new_items)
print(id(items))
print(id(new_items))