import json

data = '{"firstName": "John", "lastName": "Doe"}'

info = json.loads(data)  # convert the data in python dictionary

print(info)
print(type(info))

users = {
    "firstName" : "Jhon",
    "lastName" : "Singh",
    "email" : "jhon@gmail.com"
}

jsondata = json.dumps(users, indent=4)  # convert the python dictionary to json string

print(jsondata)