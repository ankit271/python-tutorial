import json
import requests


payload = {
    "title": "Python tutorial",
    "body": "Json and Request Modules",
    "userId": 1
}

headers = {'Content-Type': 'application/json'}

resoponse = requests.post('https://jsonplaceholder.typicode.com/posts',data= json.dumps(payload), headers=headers)

print("Response Code:", resoponse.status_code)
print("Response JSON:", resoponse.json())



#print(resoponse.status_code)
# data = resoponse.json()

# print(type(data))
# for info in data:
#     print(info['title'])
# # object (dict)
# person = {
#     "name" : "Ankit Mishra",
#     "age" : 27,
#     "address" : "Delhi"
# }

# json_data = json.dumps(person, indent=4)
# print(json_data)

# python_data = json.loads(json_data)

# print(python_data)