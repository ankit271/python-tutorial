class Employee:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Employee Name: {self.name}, Age: {self.age}"
    
    def __repr__(self):
        return f"Employee('{self.name}', {self.age})"
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
    def working(self):
        print(f"{self.name} is working.")
       
    @staticmethod 
    def isEmployee(self):
        return True if self.age > 0 else False
    
    @staticmethod
    def printHello():
        print(f"Hello")
        
    @classmethod
    def from_string(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))

emp = Employee("John Doe", 30)

emp1 = Employee.from_string("Ankit,28")
print(emp1)

#print(Employee.isEmployee(emp))

#Employee.printHello()