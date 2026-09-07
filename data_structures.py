# LIST IN PYTHON

fruits = ["apple", "banana", "orange"] 
fruits.append("mango")
print(fruits)
print(id(fruits))
print(id(fruits[0]))
print(id(fruits[1]))
print(id(fruits[2]))
print(id(fruits[3]))

numbers = [10, 20, 30] 
value = numbers.pop() 
print(value) 
print(numbers.clear())
print(numbers)

# List comprehension
even_number = [
    x for x in range(1,10)
    if x % 2 == 0
]
print(even_number)


# PRACTICAL EXAMPLE
students = ["John","Daniel","Mathew"]


# Add student using append method
students.append("Desire")


# Replace John with Elizabeth using insert method
students.insert(1,"Elizabeth")


# Display students
print(students)


# Remove John using remove method
students.remove("John")


# Count students
print(f"Numbers of Students:",len(students))


# Check whether a student exists
if "Desire" in students:
    print("student is registered")


#Sort student
students.sort()
print("Students sorted:",students)

# Fix a Duplicated email list using set method
emails = [
    "azeezsamad@email.com",
    "desire@gmail.com",
    "azeezsamad@gmail",
    "desire@gmail.com",
    "damilola@gmail.com"
]
unique_emails = set(emails)
print(unique_emails)
          
# Student Course Registration
# Consider a university with students enrolled in two courses. 
python_students = {"samad","elizabeth","desire","damilola","blessing","mariddiyyah"}
css_class = {"samad","elizabeth","damilola","blessing","ade","shola"}

# Find out students offering both courses
both_courses = python_students.intersection(css_class)
print("Students offering both courses:",both_courses)

# Find out students offering python but not css
python_only = python_students.difference(css_class)
print("Students offering python but not css:",python_only)

# Find out students offering css but not python
css_only = css_class.difference(python_students)
print("Students offering css but not python:",css_only)
# Find All unique students 
unique_students = python_students.union(css_class)
print("All unique students:",unique_students)
# Database Data Cleaning 
cities = [ 
"Lagos", 
"Ibadan", 
"Lagos", 
"Abuja", 
"Ibadan" 
]

unique_cities = set(cities)
print(unique_cities)

# User Permissions
# Suppose an application has
admin_permissions = {
    "read",
    "write",
    "delete"
}

user_permissions = {
    "read",
    "write"
}
# determine which permissions an administrator has that a normal user does not: 
admin_only_permissions = admin_permissions.difference(user_permissions)
print("Admin only permissions:", admin_only_permissions)

#  STUDENT MANAGEMENT
""" Consider a simple student management system.
1. Retrieve student 1 record
2. Retrieve student 2 score and update it
3. add student 3
    """
coursemates:dict[str,dict[str,str|int]]= {
    "stu001":{
        "name": "Azeez",
        "age": 50,
        "score": 95
    },
    "stu002":{
            "name": "Samad",
            "age": 40,
            "score": 85
    }
}
print(coursemates)
# Retriving student 1 record
print(coursemates["stu001"])
# Retrieve student 2 score and update it
coursemates["stu002"]["score"] = 100
print(coursemates["stu002"])

#
coursemates["stu003"] ={
    "name": "John",
    "age": 40,
    "score": 85
}
print(coursemates)

# MINI CHALLENGE
colleagues = [
    {"name":"samad","department": "data science","gpa": 4.24},
    {"name":"aisha","department": "computer science","gpa": 4.50},
    {"name":"john","department": "data science","gpa": 3.80}
]
# print the names of all students whose GPA is greater than 4.0
for colleague in colleagues:
    if colleague["gpa"] > 4.0:
        print(colleague["name"])
        
for colleague in colleagues:
    if colleague["department"] == "data science":
        print(colleague["name"])
        
