
#name = input("Enter your name: ")  single line comment
#age = input("Enter your age: ")

# age >= 5 addmission
# age < 5 no addmission


# conditional statements
# if, elif, else
# if( int(age) >= 5  and int(age) <= 25):
#     print("Admission granted")
# elif(int(age )< 5):
#     print("Admission not granted")
# else:
#     print("Age limit exceeded")
    
# print(f"My name is {name}. I am {age} years old.")

# range(star t, stop, step)
# for i in range(1,11,2):
#     print(i)
   
# count = 1
# while(count <= 10):
#     print(count)
#     count += 2
    
# functions, list , string

def EvenOdd(num):
    if (num %2 == 0):
        print('Number is Even')
    else:
        print('Number is Odd')


def add(a, b = 1):
    print(a + b)
    

def sumOfMarks(math, english):
    return math + english
    
#EvenOdd(5) # call
#add(5,6)
#add(5)

total = sumOfMarks(50,63)
percentage = total / 2
#print(percentage)

# firstName = "ankit"
# print(firstName)

# students = ["ankit", "saurabh", "shubham", "sagar"]

# students.append("tarun")
# students.insert(0,"ram")
# students.remove("ankit")
# students.pop()
# students.extend(["ajay","jyoti"])
# students.sort(reverse= True)
# students.clear()
# print(students)

# students = {"Ankit Mishra","Tarun Singh"}
# students1 = {"Subu Singh", "Ankit Mishra"}
# ankit, tarun, subu = students
# print(ankit)
# print(tarun)
#students.add("Ajay")
#students.remove("Ankit Mishra")
#students.update(["Ajay", "Jyoti"])
#students.remove("Ankit")

#print(students.union(students1))
#print(students.intersection(students1))
# print(students.difference(students1))

person = {    
    "age" : 25,    
    "address" : "Delhi"
}

print(person.keys())     # Output: dict_keys(['name', 'age', 'city', 'email'])
# Output: dict_values(['Alice', 31, 'New York', 'alice@email.com'])
print(person.values())
print(person.items())
