students = [
        {"name": "Samad", "score": 85},
        {"name": "Aisha", "score": 45},
        {"name": "John", "score": 72},
        {"name": "Mary", "score": 38},
        {"name": "David", "score": 91}
        ]

# function 1
def calculate_average(students):
    total = 0
    for student in students:
        total += student["score"]
        average = total / len(students)

    return average

result = calculate_average(students)
print(result)

# function 2
def count_passed(students):
        passed = 0
        for student in students:
            if student["score"] >= 50:
                passed += 1

        return passed

results = count_passed(students)
print(results)

# function 3
def get_excellent_score(students):
    excellent = []

    for student in students:
        if student["score"] >= 70:
            excellent.append(student["name"])

    return excellent 
grade = get_excellent_score(students)
print(grade)