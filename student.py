class Student:
    
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age})"
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
ankit = Student("Ankit", 21)    
print(ankit.name)