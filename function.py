
# def getWelcome(**kargs):    
#     for val in kargs.values():
#         print(f"{val}")
    
    
# getWelcome(first = "Ankit", fifth = "Sumit")

# def getCountry(country = "India"):
#     print(f"Country is: {country}")

# getCountry("USA")

# def getTotalMarks(math, english):
#     total = math + english 
#     return total

# total = getTotalMarks(90, 80)
# print(f"Total Marks: {total}")

# print("Average Marks: ", total/2)


def outer_function():    
    def inner_function():        
        name = "python"
        return name        
    return inner_function()
        

data = outer_function()
print(data)

