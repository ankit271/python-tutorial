class Employee:
    
    salary_increment = 1.05  # Class variable    
    
    def __init__(self,first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@gmail.com'
        self.salary = salary
        
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def display(self):
        print('Employee Name: {}'.format(self.full_name()))
        print('Employee Email: {}'.format(self.email))
        print('Employee Salary: {}'.format(self.salary))
    
    def apply_increment(self):
       self.salary = (self.salary * self.salary_increment)
       return self.salary


class Developer(Employee):
   
    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary)
        self.programming_language = programming_language
        
    def display(self):
        super().display()
        print('Employee Programming Language: {}'.format(self.programming_language))

class Manager(Employee):

      def __init__(self, employees=None):
            if employees is None:
                employees = []
            else:
                employees = [employees]
                                
            self.employees = employees
            
      def add_employee(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)
                
      def remove_employee(self, emp):
            if emp in self.employees:
                self.employees.remove(emp) 
                
      def display(self):
          for emp in self.employees:
              print('Employee Name: {}'.format(emp.full_name()))
       
prog_1 = Developer('John', 'Doe', 50000, 'Python')
prog_2 = Developer('Johnny', 'Doe', 60000, 'C++')

mgr1 = Manager(prog_1)
# mgr1.add_employee(prog_1)
# mgr1.add_employee(prog_2)
# mgr1.display()
# mgr1.remove_employee(prog_1)
##mgr1.display()