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



