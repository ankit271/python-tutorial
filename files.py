from logger import logMessage 

try:
    with open("demo1.txt", "r") as file:
        content = file.read()
        print(content)
        
except Exception as e:    
    logMessage(e)
finally:
    print("File reading operation completed.")
