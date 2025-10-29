
users = { 
            "firstName": "Ankit",
            "lastName" : "Mishra" ,
            "address" : {
                "street": "123 Main St",
                "city": "New York",
                "state": "NY"
            }
        }
            
        

#users["firstNam"] = "Sumit"
#users.update({"firstNam": "Sumit"})

#print(users.get("firstName"))

#users.pop("firstName");
#print(users["firstName"])

for key, value in  users.items():
    print(key + " : " + str(value))

#print(users)
print(users["address"]["city"])