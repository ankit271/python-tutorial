import json

# Python dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Convert the Python dictionary to a JSON string
# json_string = json.dumps(person,indent=4)
# print(json_string)

with open("user.json", "w") as file:
    json.dump(person, file, indent=4)

# json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# # # Convert the JSON string to a Python dictionary
# person = json.loads(json_string)
# print(person)
