
user = {
    "name" : "Ankit",
    "age" : 28
}

# user["name"] = "Roli Gupta"

# user["isGirl"] = True
# del user["age"]

user.update({"name" : "Roli Gupta"})
for key in user:
    print(key, user[key])