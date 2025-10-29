import traceback

try:
    age = int(input("Enter your age "))
    if age < 18:
        raise ValueError("Age must be at least 18.")
    print("You are eligible to vote.")
except ValueError as e:
    print(f"Invalid input: {e}")    

# try:
#     with open("sampl.txt", "r") as file:        
#         content = file.read()
#         print(content)
# except Exception as e:
#     print(f"File not found. {e}")
#     traceback.print_exc()
# finally:
#     print("Execution completed.") 
