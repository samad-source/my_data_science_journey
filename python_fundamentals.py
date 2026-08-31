#Create a calculator that asks the user for two numbers and performs basic arithmetic.

num1 = float(input("Enter the first num: "))
num2 = float(input("Enter the second num: "))

print(f"Subtraction: {num1 - num2}")
print(f"Addition: {num1 + num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Remainder: {num1 % num2}")

# Login Validation

username = input("Enter your username: ")
password = int(input("Enter your password: "))

if username == "admin" and password == 1234:
    print("LOGIN SUCCESSFUL : WELCOME BACK TO FACEBOOK")
else:
    print("kindly enter the correct password")

# Student Grading System

score = float(input("Enter the student's score and let the system determine the grade: "))

if score >= 70:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 50:
    grade = 'C'
elif score >= 40:
    grade = 'D'
else:
    grade = 'F'

print(f"The grade for {score} = {grade}")

# Name Processing Program
name = input("Enter your full name: ")
clean_name = name.strip().title()
print(f"welcome, {clean_name}!!!")

# Email Validation
email = input("Enter your Email address: ")
if "@" in email and "." in email:
    print("Email format look valid")
else:
    print("Invalid Email Address")

# Word Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Number of word: {len(words)}")

#Password Length Check 
password = input("Enter your password: ")
if len(password) >= 8:
    print("Password Correct")
else:
    print(f"Password is too short")