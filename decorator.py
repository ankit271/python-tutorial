class Student:
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name        
   
    @property 
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    @property 
    def email(self):
        return f'{self.first_name}.{self.last_name}@school.com'
    
    @email.setter
    def email(self, newValue):        
        self.email = newValue
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first_name = None
        self.last_name = None
        
std = Student('John', 'Doe')  
std.first_name = 'Jane'

print(std.email)

del std.fullname
print(std.fullname)
