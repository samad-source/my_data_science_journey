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

